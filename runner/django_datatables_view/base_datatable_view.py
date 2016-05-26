# -*- coding: utf-8 -*-

import logging

from django.conf import settings
from django.db.models import Q
from django.utils.translation import ugettext as _
from django.core import serializers
from django.core.exceptions import ImproperlyConfigured
from .mixins import JSONResponseView

logger = logging.getLogger(__name__)


class DatatableMixin(object):
    """ JSON data for datatables
    """
    model = None
    columns = []
    order_columns = []
    max_display_length = 100  # max limit of records returned, do not allow to kill our server by huge sets of data
    pre_camel_case_notation = False  # datatables 1.10 changed query string parameter names
    use_get_display = True
    
    def initialize(self, *args, **kwargs):
        if 'iSortingCols' in self.request.REQUEST:
            self.pre_camel_case_notation = True

    def get_order_columns(self):
        """ Return list of columns used for ordering
        """
        return self.order_columns

    def get_columns(self):
        """ Returns the list of columns that are returned in the result set
        """
        return self.columns

    def render_column_old(self, row, column):
        """ Renders a column on a row
        """
        if hasattr(row, 'get_%s_display' % column):
            # It's a choice field
            text = getattr(row, 'get_%s_display' % column)()
        else:
            try:
                text = getattr(row, column)
            except AttributeError:
                obj = row
                for part in column.split('.'):
                    if obj is None:
                        break
                    obj = getattr(obj, part)

                text = obj

        if hasattr(row, 'get_absolute_url'):
            return '<a href="%s">%s</a>' % (row.get_absolute_url(), text)
        else:
            return text

    def render_column(self, row, columns):
        data = {}
        
        for column in columns:
            if hasattr(row, 'get_%s_display' % column) and self.use_get_display:
                # It's a choice field
                text = getattr(row, 'get_%s_display' % column)()
            else:
                try:
                    text = getattr(row, column)
                except AttributeError:
                    logger.error("row=%s column=%s"% (row, column))
                    obj = row
                    for part in column.split('.'):
                        if obj is None:
                            break
                        
                        try:
                            obj = getattr(obj, part)
                        except AttributeError as e:
                            raise ImproperlyConfigured('Error! "{}" is not a field of "{}" ({}). Please remove it from "columns" or define a custom behaviour overriding "render_column"'.format(part, obj, obj.__class__))

                    text = obj


            if hasattr(row, 'get_absolute_url'):
                text= '<a href="%s">%s</a>' % (row.get_absolute_url(), text)

            data.update({column:text})

        return data
        
    def ordering(self, qs):
        """ Get parameters from the request and prepare order by clause
        """
        request = self.request

        # Number of columns that are used in sorting
        sorting_cols = 0
        if self.pre_camel_case_notation:
            try:
                sorting_cols = int(request.REQUEST.get('iSortingCols', 0))
            except ValueError:
                sorting_cols = 0
        else:
            sort_key = 'order[{0}][column]'.format(sorting_cols)
            while sort_key in self.request.REQUEST:
                sorting_cols += 1
                sort_key = 'order[{0}][column]'.format(sorting_cols)

        order = []
        order_columns = self.get_order_columns()

        for i in range(sorting_cols):
            # sorting column
            sort_dir = 'asc'
            try:
                if self.pre_camel_case_notation:
                    sort_col = int(request.REQUEST.get('iSortCol_{0}'.format(i)))
                    # sorting order
                    sort_dir = request.REQUEST.get('sSortDir_{0}'.format(i))
                else:
                    sort_col = int(request.REQUEST.get('order[{0}][column]'.format(i)))
                    # sorting order
                    sort_dir = request.REQUEST.get('order[{0}][dir]'.format(i))
            except ValueError:
                sort_col = 0

            sdir = '-' if sort_dir == 'desc' else ''
            sortcol = order_columns[sort_col]

            if isinstance(sortcol, list):
                for sc in sortcol:
                    order.append('{0}{1}'.format(sdir, sc.replace('.', '__')))
            else:
                order.append('{0}{1}'.format(sdir, sortcol.replace('.', '__')))

        if order:
            return qs.order_by(*order)
        return qs

    def paging(self, qs):
        """ Paging
        """
        if self.pre_camel_case_notation:
            limit = min(int(self.request.REQUEST.get('iDisplayLength', 10)), self.max_display_length)
            start = int(self.request.REQUEST.get('iDisplayStart', 0))
        else:
            limit = min(int(self.request.REQUEST.get('length', 10)), self.max_display_length)
            start = int(self.request.REQUEST.get('start', 0))

        # if pagination is disabled ("paging": false)
        if limit == -1:
            return qs

        offset = start + limit

        return qs[start:offset]

    def get_initial_queryset(self):
        if not self.model:
            raise NotImplementedError("Need to provide a model or implement get_initial_queryset!")
        return self.model.objects.all()

    def extract_datatables_column_data(self):
        """ Helper method to extract columns data from request as passed by Datatables 1.10+
        """
        request_dict = self.request.REQUEST
        col_data = []
        if not self.pre_camel_case_notation:
            counter = 0
            data_name_key = 'columns[{0}][name]'.format(counter)
            while data_name_key in request_dict:
                searchable = True if request_dict.get('columns[{0}][searchable]'.format(counter)) == 'true' else False
                orderable = True if request_dict.get('columns[{0}][orderable]'.format(counter)) == 'true' else False

                col_data.append({'name': request_dict.get(data_name_key),
                                 'data': request_dict.get('columns[{0}][data]'.format(counter)),
                                 'searchable': searchable,
                                 'orderable': orderable,
                                 'search.value': request_dict.get('columns[{0}][search][value]'.format(counter)),
                                 'search.regex': request_dict.get('columns[{0}][search][regex]'.format(counter)),
                                 })
                counter += 1
                data_name_key = 'columns[{0}][name]'.format(counter)
        
        return col_data

    def filter_queryset(self, qs):
        """ If search['value'] is provided then filter all searchable columns using istartswith
        """
        if not self.pre_camel_case_notation:
           
            # get global search value
            search = self.request.GET.get('search[value]', None)
            logger.info("SEARCH=%s"%search)
            
            col_data = self.extract_datatables_column_data()
            q = Q()
            for col_no, col in enumerate(col_data):
                # apply global search to all searchable columns
                if search and col['searchable']:
                    q |= Q(**{'{0}__istartswith'.format(self.columns[col_no]): search})

                # column specific filter
                if col['search.value']:
                    qs = qs.filter(**{'{0}__istartswith'.format(self.columns[col_no]): col['search.value']})
            qs = qs.filter(q)
        return qs

    def prepare_results(self, qs):
        data = []
#        if not self.dt_editor:
#            for item in qs:
#                data.append([self.render_column(item, column) for column in self.get_columns()])
#            return data
#        else:
        for item in qs:
            data.append(self.render_column(item, self.get_columns()))
        return data

    def get_context_data(self, *args, **kwargs):
        request = self.request
        try:
            self.initialize(*args, **kwargs)

            qs = self.get_initial_queryset()

            # number of records before filtering
            total_records = qs.count()

            qs = self.filter_queryset(qs)

            # number of records after filtering
            total_display_records = qs.count()

            qs = self.ordering(qs)
            qs = self.paging(qs)

            # prepare output data
            if self.pre_camel_case_notation:
                aaData = self.prepare_results(qs)

                ret = {'sEcho': int(request.REQUEST.get('sEcho', 0)),
                       'iTotalRecords': total_records,
                       'iTotalDisplayRecords': total_display_records,
                       'aaData': aaData
                       }
            else:
                data = self.prepare_results(qs)

                ret = {'draw': int(request.REQUEST.get('draw', 0)),
                       'recordsTotal': total_records,
                       'recordsFiltered': total_display_records,
                       'data': data
                }
        except Exception as e:
            logger.exception(str(e))

            if settings.DEBUG:
                import sys
                from django.views.debug import ExceptionReporter
                reporter = ExceptionReporter(None, *sys.exc_info())
                text = "\n" + reporter.get_traceback_text()
            else:
                text = "\nAn error occured while processing an AJAX request."

            if self.pre_camel_case_notation:
                ret = {'result': 'error',
                       'sError': text,
                       'text': text,
                       'aaData': [],
                       'sEcho': int(request.REQUEST.get('sEcho', 0)),
                       'iTotalRecords': 0,
                       'iTotalDisplayRecords': 0,}
            else:
                ret = {'error': text,
                       'data': [],
                       'recordsTotal': 0,
                       'recordsFiltered': 0,
                       'draw': int(request.REQUEST.get('draw', 0))}
        
#        logger.info("RET=%s"%ret)
        return ret


class BaseDatatableView(DatatableMixin, JSONResponseView):
    pass