

(function($) {
    $.fn.generateScreen = function(liste)
    {
        this.each(function() {
            var concat="";
            var token2='{% csrf_token %}';
            for(var parameter in liste) {


                if(parameter=="classC"){

                    concat=concat+"<div class='"+liste.classC+"'><h1>Moncontainer</div> " ;

                    $( this ).append( concat ); 
                    //concat="";
                }else{
                    concat="";
                }


                if(parameter=="classB"){

                    /*  if (liste.title == "undefined"){ demain voir comment mettre valeur si pas rien
	   *     alert("pas definie");
	   *     
	}*/;
                    concat=concat+"<div id="+liste.idJumb+" class='"+liste.classB+"'><h1>"+liste.title+"</h1><p>"+liste.contenu+"</p><p></div> " ;

                    $( "#"+liste.idCont+"" ).append( concat ); 
                    //concat="";
                }else{
                    concat="";
                }
                ;

                if(parameter=="classButton"){
                    // concat="";// voir apres si laisser ici

                    concat=concat+"<a href="+liste.url+" class='"+liste.classButton+"' >Fork this fiddle</a></p>";

                    $( "#"+liste.idJumb+"" ).append( concat ); 
                    //  concat="";
                }else{
                    concat="";
                }
                ;



                // generate fields
                if(parameter=="fields"){
                    alert("ok")
                    var formulaire=liste.fields;

                    concat+="<form method='post' class='' action='/reselling/26000/updateJuri/'> "   
                    concat+=token
                    concat+="<legend>update destination </legend> <div class=''>"
                    for (param in formulaire){
                        
                        concat+="<label   for='usr'>"+param+":</label><input class='input-xlarge' type='text'  placeholder='.input-xlarge' value="+formulaire[param]+"><br>"
            

                    }

                    concat+="<input type='submit' value='Envoyer'  class='btn btn-primary' /></div>";
                    concat+="<form>"   

                    $( this).append( concat ); 
                }
                else{
                    concat="";

                }
                ;



                if(parameter=="button"){

                    var button=liste[parameter];
                    for (param in button){
                        concat+="<a href='a' class='"+button[param]+"' >Primary</a>";
                        //button[param]="";
                    }

                    $("#"+liste.idJumb+"" ).append( concat ); 
                    // concat="";
                }
                else{

                    concat="";
                }
                ;
            }
        });
        return this;
    };
})(jQuery);

