$(document).ready(function(){  // generateMenu();

    // generateMenu();
    function generateMenu(){



        var concat="" ;
        var  menu = {

            "dashboard": ' {% url "reselling:dashboard" %}',
            "achats": '{% url "reselling:achats" %}',
            "travaux": '{% url "reselling:travaux" %}'


        }




        $.each(menu, function (key, data) {

            concat =   "<li class='launcher'>"+
                " <i class='fa fa-exclamation '></i>"+
                " <a href="+data+">"+key+"</a>"+
                " </li>"+concat;

        })

        // console.log(concat);

        var  settings="<ul id='dock'> "+concat+" </ul>";

        $('#sidebar').prepend(settings);


    }



    // to do creer fonction 

    // script changement de background //



    $('body').on('click', '.test', function(e){
        e.preventDefault();

        //    $('#boost').replaceWith("");
        $('#boost').replaceWith( '<link id="boost" rel="stylesheet" type="text/css" href="{% static "reselling/css/bootstrap.css" %}" />');


    });



    var concat ;
    var img = {

        "img": '{% static "reselling/images/logo_nerim.png" %}',
        "img2": '{% static "reselling/images/skin-violate.jpg" %}',
        "img4": '{% static "reselling/images/skin-violate.jpg" %}',
        "img5": '{% static "reselling/images/777.gif" %}',
        "img3": '{% static "reselling/images/profile.png"" %}'


    }

    // to do splint url poru recupere img ou redimensionnement de l'image
    $.each(img, function (key, data) {


        concat='<a data-skin="skin-blur-violate" class="col-sm-2 col-xs-4" href="">' +
            '<img src='+data+' alt="">' +
            '</a>'+concat;

    })


    var settings =  '<a id="settings" href="#changeSkin" data-toggle="modal">' +
        '<i class="fa fa-gear"></i> Change Skin' +
        '</a>' +   
        '<div class="modal fade" id="changeSkin" tabindex="-1" role="dialog" aria-hidden="false">' +
        '<div class="modal-dialog modal-lg">' +
        '<div class="modal-content">' +
        '<div class="modal-header">' +
        '<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>' +
        '<h4 class="modal-title">Changer le fond </h4>' +
        '</div>' +
        '<div class="modal-body">' +
        '<div class="row template-skins">' +

        concat+	

        '</div>' +
        '</div>' +
        '</div>' +
        '</div>' +
        '</div>';



    $('#main').prepend(settings);

    $('body').on('click', '.template-skins > a', function(e){
        e.preventDefault();
        var skin = $(this).attr('data-skin');

        $('body').attr('id', skin);
        $('#changeSkin').modal('hide');
    });

 

    $(document).ajaxStart(function(){ // Nous ciblons l'élément #loading qui est caché
        
        
         $('body #sidebar').on('click', 'a', function(e){

        $("body").append('<div class=" jumbotron text-center  chargement"> <h2 class="visible-lg">Chargement </h2><h3 class="visible-xs">Chargement </h3></div>  ')

        })
    });


    linkactive()
    // toggle pour le sidebar lorsque le menu est en responsive  //
    function linkactive(){
        $('[data-toggle="offcanvas"]').click(function () {
            $('.row-offcanvas').toggleClass('active')
        });

        var host=document.location.host;
        // permet de rester hover sur le lien active 
        var url = jQuery(location).attr("href"); 
        var res = url.split(host); // a changer par la suite 
        var url=res[1];
        ///  alert(document.location.host);
        var res2 = url.split("/");
        var res2=res2[2];

        $("#nomPanel").replaceWith('<div id="nomPanel"><i class=" fa fa-long-arrow-right fa-fw"></i>'+res2);
        $("#nomPanel").hide();
        $("#nomPanel").fadeIn(1000);

        $("#dock li a").each(function(){
            if(url==$(this).attr("href")){
                $(this).parent().addClass("active");

            }
        });

    }

    // toggle pour le sidebar lorsque le menu est en responsive  
});