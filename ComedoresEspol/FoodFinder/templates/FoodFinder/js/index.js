
function filtro(criterio, orden){
	var platillos = document.getElementsByClassName("platillo");
	var lista = [];

	var i;
	var j;
	for (i = 0; i < platillos.length; i++) { 
		platillos[i].style.display = "block";
		lista.push(platillos[i].getAttribute(criterio));
	}
	if(orden == "asc"){
		lista.sort(function(a, b){return b-a});
	}
	else{
		lista.sort();
	}
	for(j = 0; j < lista.length; j++) { 
		for (i = 0; i < platillos.length; i++) { 
			if(platillos[i].getAttribute(criterio) == lista[j]){
				platillos[i].style.order = ""+j+"";
			}
		}
	}

	if(criterio == "data-disponible"){
		for (i = 0; i < platillos.length; i++) { 
			if(platillos[i].getAttribute(criterio) =="no"){
				platillos[i].style.display = "none";
			}
		}
	}

	console.log(lista);

}


function cargarPlatillos() {
	$.getJSON("data/platillos.json", function(data) {
		$.each(data, function(key, val) {
			var div = $('<div></div>');
			var desc = $('<div></div>');
			var imag = $('<img />');
			var tit = $('<h4></h4>');
			var lista = $('<ul></ul>');
			var prec = $('<li></li>');
			var like = $('<li></li>');
			var disp = $('<li></li>');
			div.attr("data-precio",val["precio"]);
			div.attr("data-vNutricional",val["nutricion"]);
			div.attr("data-disponible",val["disponible"]);
			div.attr("data-distancia",val["distancia"]);
			div.attr("class","platillo");
			desc.attr("class","desc");
			imag.attr("src",val["imagen"]);
			imag.attr("width","250");
			tit.append(val["titulo"]);
			prec.append("<span class='glyphicon glyphicon-apple'></span> ");
			prec.append(" $ "+ val["precio"]);
			like.append("<span class='glyphicon glyphicon-map-marker'></span> ");
			like.append(val["distancia"] + " mts");
			if( val["disponible"] == "si"){
				disp.append("<span class='glyphicon glyphicon-ok'></span> ");
				disp.append(" Aun disponible");
			}else{
				disp.append("<span class='glyphicon glyphicon-remove'></span> ");
				disp.append(" Agotado");
			}
			lista.append(prec);
			lista.append(like);
			lista.append(disp);
			desc.append(tit);
			desc.append(lista);
			div.append(desc);
			div.append(imag);
			$('.platillos-del-dia').append(div);
		});
    });
}






$( document ).ready(function() {
   cargarPlatillos();
});