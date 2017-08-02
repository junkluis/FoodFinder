var map;
var marker;
var miPosicion;

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
        console.log("Geolocation is not supported by this browser.");
    }
}

function showPosition(position) {
	let icono = 'https://www.royalparks.org.uk/_media/images/map_icons/find-my-location-icon.png';
	let lat = position.coords.latitude;
	let lon = position.coords.longitude;
	miPosicion = new google.maps.LatLng(lat,lon);
	let pos = new google.maps.Marker({
		position: miPosicion,
		icon: icono,
		title: 'Mi posicion',});
	pos.setMap(map);
}