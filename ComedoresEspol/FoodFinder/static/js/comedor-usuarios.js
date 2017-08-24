setInterval(function() {
    jQuery.ajax({
        url: "/FoodFinder/refresh",
        dataType: "json",
        type: 'GET',
        success: function (datos) {
            platos = datos.platillos;
        },
        error: function(XMLHttpRequest, textStatus, errorThrown){
            console.log(errorThrown);
        }
    });
    var tabla = [];
    var header =  ['Platillo', 'Puntuación ',  { role: 'style' },{ role: 'annotation' },];
    tabla.push(header);
    var i = 0;

    var colores = ['#C02942','#D95B43','#D95B43','#ECD078','#53777A']
    for(i; i<platos.length; i++){
        infoP = platos[i];
        tabla.push([infoP.nombre, infoP.valoracion, colores[i], infoP.valoracion]);
    }


    google.charts.load('current', {packages: ['corechart', 'bar']});
    google.charts.setOnLoadCallback(BarChart);

    function BarChart() {

          var data = google.visualization.arrayToDataTable(tabla);

          var options = {
            chartArea: {width: '50%'},
            hAxis: {
              title: 'Puntuación',
              minValue: 0
            },
            vAxis: {
              title: 'Platillos'
            },
            width: 1200,
            height: 400,
            bar: {groupWidth: "80%"},
            legend: { position: "none" },
          };
          var chart = new google.visualization.BarChart(document.getElementById('chart_div'));

          chart.draw(data, options);
        }

}, 500);
