var map;
var marker;
var miPosicion;
var lat;
var lon;

function iniciarMapa() {
	//coordernadas iniciales
	let coord = new google.maps.LatLng(-2.1473363,-79.9655131);
	//propiedades del mapa
	var mapProp= {
	    center:coord,
	    zoom:17,
	    disableDefaultUI: true,
	};
	//Crea el mapa en el Div con el id mapa-comedores
	map = new google.maps.Map(document.getElementById("mapa-comedores"),mapProp);
	//Crea un marcador de google en la posicion de las coordenadas
	marker = new google.maps.Marker({position: coord});
	//coloca el marcador en el mapa
	marker.setMap(map);
	getLocation();
}

function selecComed(lat, long, nombre){
	marker.setMap(null);
	let coord=new google.maps.LatLng(lat,long);
	marker = new google.maps.Marker({position: coord});
	var infowindow = new google.maps.InfoWindow({
          content: nombre
        });
	marker.addListener('click', function() {
          infowindow.open(map, marker);
        });
	marker.setMap(map);
	map.setCenter(coord);
}

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else { 
        alert("La geolocalizacion no es soportada por este explorador.");
    }
}

function showPosition(position) {
	let icono = 'https://www.royalparks.org.uk/_media/images/map_icons/find-my-location-icon.png';
	lat = position.coords.latitude;
	lon = position.coords.longitude;
	miPosicion = new google.maps.LatLng(lat,lon);
	console.log(miPosicion);
	let pos = new google.maps.Marker({
		position: miPosicion,
		icon: icono,
		title: 'Mi posicion',});
	pos.setMap(map);
}

window.onload=function() {
	var comedores = document.getElementsByClassName("comedor-tk");
	let latC;
	let lonC;
	let distancias = [];
	for(var i=0; i<comedores.length; i++){
		let indexDistance = []
		latC = comedores[i].getAttribute("data-lat")
		lonC = comedores[i].getAttribute("data-lon")
		var distance = getDistance(lat, lon, latC, lonC);
		distancias.push(distance);
		let distaRounded = Math.round(distance * 100) / 100
		comedores[i].setAttribute("data-distance",distance);
		comedores[i].childNodes[5].childNodes[1].innerHTML = "<b>Distancia:</b> " + distaRounded + " mts.";
	}
	distancias.sort();
	console.log(distancias);

	for(j = 0; j < comedores.length; j++) {
		for (i = 0; i < distancias.length; i++) {
			if(comedores[i].getAttribute("data-distance") == distancias[j]){
				comedores[i].style.order = ""+j+"";
			}
		}
	}

}

var rad = function(x) {
  return x * Math.PI / 180;
};

var getDistance = function(lat1, lon1, lat2, lon2) {
  var R = 6378137;
  var dLat = rad(lat2 - lat1);
  var dLong = rad(lon2 - lon1);
  var a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
    Math.cos(rad(lat1)) * Math.cos(rad(lat2)) *
    Math.sin(dLong / 2) * Math.sin(dLong / 2);
  var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
  var d = R * c;
  return d;
};