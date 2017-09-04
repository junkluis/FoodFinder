function ActualizarPerfil(){
	
	var descrip = jQuery("#Act-descripcion").val();
	var especialidad = jQuery("#Act-especialidad").val();
	var facultad = jQuery("#Act-facultad").val();
	var ayudantes = jQuery(".toggle ").hasClass("off");
	var comedorPk = jQuery(".comedorAdmin").attr("data-pk");
	

	jQuery.ajax({
              url: "/FoodFinder/admin/actualizarInfo",
              dataType: "json",
              data: {
              	descrip: descrip,
              	especialidad: especialidad,
              	facultad: facultad,
              	ayudantes: ayudantes,
              	comedorPk: comedorPk,
              },
              type: 'GET',
              error: function(XMLHttpRequest, textStatus, errorThrown){
                  console.log(errorThrown);
              },
              success: function(data){
              	jQuery("#InfoDesc").text(data["descrip"]);
              	jQuery("#InfoHora").text(data["descrip"]);
              	jQuery("#InfoTipo").text(data["especialidad"]);
              	jQuery("#InfoFacTNombre").text(data["Nombrefac"]);
              	if(data["ayudantes"] == "true"){
					jQuery("#InfoAyudantes").text("No se aceptan ayudantes");
              	}
              	else{
					jQuery("#InfoAyudantes").text("Se aceptan ayudantes");
              	}
              	

              }
          });
}