
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

$( document ).ready(function() {
   console.log("hola desde index");
});