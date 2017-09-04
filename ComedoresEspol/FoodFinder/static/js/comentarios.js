function mostrarCuadroEditar(id){
	$(".editarComentario").attr("id",id);
	jQuery.ajax({
			url: "/FoodFinder/mostrarEditarComentario/"+id,
			method: 'GET',
			success: function (data) {
				document.getElementById("usuario").innerHTML=data["usuario"];
				document.getElementById("comedor").innerHTML=data["comedor"];
				document.getElementById("comentario").innerHTML=data["comentario"];
			},
			error: function(XMLHttpRequest, textStatus, errorThrown){
				console.log(errorThrown);
			}
		});
		$("#div_editar").show();
}
function eliminarComentario(id){
	jQuery.ajax({
			url: "/FoodFinder/eliminarComentario/"+id,
			type: 'DELETE',
			success: function (data) {
				$('#comentario'+id).hide()
			},
			error: function(XMLHttpRequest, textStatus, errorThrown){
				console.log(errorThrown);
			}
		});
}
function editarComentario(id){
	var comentario=document.getElementById("comentario").value;
	jQuery.ajax({
			url: "/FoodFinder/editarComentario/",
			type: 'Get',
			data: {
				'idComen': id,
				'comentario': comentario
			},
			success: function (data) {
				document.getElementById("comentario").innerHTML=data["comentario"];
			},
			error: function(XMLHttpRequest, textStatus, errorThrown){
				console.log(errorThrown);
			}
		});
}
function aceptarComentario(id){
	jQuery.ajax({
			url: "/FoodFinder/aceptarComentario/",
			type: 'GET',
			data: {
				'idComen': id,
			},
			success: function (data) {
				$('#comentario'+id).hide();
			},
			error: function(XMLHttpRequest, textStatus, errorThrown){
				console.log(errorThrown);
			}
		});
}
