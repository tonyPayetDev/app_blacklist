# install app_blacklist

creer environnement virtuel avec virtualenvs

mkvirtualenv blacklist

workon blacklist

pip install -r requirements_news.txt

python manage.py syncdb

python manage.py runserver
