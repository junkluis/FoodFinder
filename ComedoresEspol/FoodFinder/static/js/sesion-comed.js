var newMarker;
var newLat;
var newLon;

function ActualizarPerfil(){
  
  var descrip = jQuery("#Act-descripcion").val();
  var especialidad = jQuery("#Act-especialidad").val();
  var facultad = jQuery("#Act-facultad").val();
  var ayudantes = jQuery(".toggle ").hasClass("off");
  var comedorPk = jQuery(".comedorAdmin").attr("data-pk");
  var horaInicio = jQuery("#Act-horaInicio").val();
  var horaCierre = jQuery("#Act-horaCierre").val();

  jQuery.ajax({
    url: "/FoodFinder/admin/actualizarInfo",
    dataType: "json",
    data: {
                descrip: descrip,
                especialidad: especialidad,
                facultad: facultad,
                ayudantes: ayudantes,
                comedorPk: comedorPk,
                horaInicio: horaInicio,
                horaCierre: horaCierre,
              },
              type: 'GET',
              error: function(XMLHttpRequest, textStatus, errorThrown){
                  console.log(errorThrown);
              },
              success: function(data){
                jQuery("#InfoDesc").text(data["descrip"]);
                jQuery("#InfoHora").text(data["hora_ini"] + " - " + data["hora_fin"]  );
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

function initMap() {
        var latitud = parseFloat(jQuery(".comedorAdmin").attr("data-lat"));
        var longitud = parseFloat(jQuery(".comedorAdmin").attr("data-lon"));
        var uluru = {lat: latitud, lng: longitud};
        var map = new google.maps.Map(document.getElementById('miUbicacion'), {
          zoom: 16,
          center: uluru,
          disableDefaultUI: true,
        });
        var map2 = new google.maps.Map(document.getElementById('nuevaUbicacion'), {
          zoom: 16,
          center: uluru,
          disableDefaultUI: true,
        });
        var marker = new google.maps.Marker({
          position: uluru,
          map: map
        });
        newMarker = new google.maps.Marker({
          position: uluru,
          map: map2
        });
      }


      function setUbicacion() {
        var map = new google.maps.Map(document.getElementById('nuevaUbicacion'), {
          center: {lat: -34.397, lng: 150.644},
          zoom: 16,
          disableDefaultUI: true,
        });

        if (navigator.geolocation) {
          navigator.geolocation.getCurrentPosition(function(position) {
            newLat = position.coords.latitude;
            newLon = position.coords.longitude;

            var pos = {
              lat: position.coords.latitude,
              lng: position.coords.longitude
            };

            newMarker = new google.maps.Marker({
              position: pos,
              map: map
            });

            map.setCenter(pos);
          });
        } else {
          handleLocationError(false, infoWindow, map.getCenter());
        }
      }

      function handleLocationError(browserHasGeolocation, infoWindow, pos) {
        infoWindow.setPosition(pos);
        infoWindow.setContent(browserHasGeolocation ?
                              'Error: The Geolocation service failed.' :
                              'Error: Your browser doesn\'t support geolocation.');
      }


function guardarNuevaUbicacion(Oldlat, Oldlot){

  var comedorPk = jQuery(".comedorAdmin").attr("data-pk");

  if(newLat == null || newLon == null){
    newLat = Oldlat;
    newLon = Oldlot;
  }

  jQuery.ajax({
              url: "/FoodFinder/admin/actualizarUbicacion",
              dataType: "json",
              data: {
                newLat: newLat,
                newLon: newLon,
                comedorPk:comedorPk,
              },
              type: 'GET',
              error: function(XMLHttpRequest, textStatus, errorThrown){
                  console.log(errorThrown);
              },
              success: function(data){
                
              }
          });

}