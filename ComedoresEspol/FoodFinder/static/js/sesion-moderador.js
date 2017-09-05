function editarPerfil(){

	var usuarioId = jQuery("#usuarioId").val();
	var nombre = jQuery("#nombre").val();
    console.log(nombre);
	var apellido = jQuery("#apellido ").val();
    console.log(apellido);
	var correo = jQuery("#correo").val();
    console.log(correo);
	var rol = jQuery("#rol").val();
    console.log(rol);

	jQuery.ajax({
              url: "/FoodFinder/moderador/modificarUsuario",
              dataType: "json",
              data: {
              	usuarioId: usuarioId,
              	nombre: nombre,
              	apellido: apellido,
              	correo: correo,
                rol: rol
              },
              type: 'GET',
              error: function(XMLHttpRequest, textStatus, errorThrown){
                  console.log(errorThrown);
              },
              success: function(data){
              	jQuery("#nombreU").text(data["nombre"]);
              	jQuery("#apellidoU").text(data["apellido"]);
              	jQuery("#correoU").text(data["correo"]);
                jQuery("#rolU").text(data["rol"]);


              }
          });
}
