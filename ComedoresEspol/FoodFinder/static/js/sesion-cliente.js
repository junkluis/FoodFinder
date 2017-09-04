function EditarPerfil(){

	var usuarioId = jQuery("#usuarioId").val();
	var nombre = jQuery("#nombre").val();
    console.log(nombre);
	var apellido = jQuery("#apellido ").val();
    console.log(apellido);
	var correo = jQuery("#correo").val();
    console.log(correo);
    var facultad = jQuery("#facultad").val();
    console.log(facultad);
	var rol = jQuery("#rol").val();
    console.log(rol);

	jQuery.ajax({
              url: "/FoodFinder/cliente/modificarUsuario",
              dataType: "json",
              data: {
              	usuarioId: usuarioId,
              	nombre: nombre,
              	apellido: apellido,
              	correo: correo,
                facultad: facultad,
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
              	jQuery("#facultadU").text(data["facultad"]);
                jQuery("#rolU").text(data["rol"]);


              }
          });
}
