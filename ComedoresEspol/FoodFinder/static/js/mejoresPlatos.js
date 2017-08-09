/*jQuery( document ).ready(function() {
   arreglo();
});


var data = [{
                "name": "Arroz  luis con Pollo",
                "value": 20,
                "image": "../img/logo.png"
        },
            {
                "name": "Lasaña de Carne",
                "value": 12,
 				"image": "../img/logo.png"               
        },
            {
                "name": "Pollo con Champiñones",
                "value": 19,

        },
            {
                "name": "Costillas BBQ",
                "value": 5,
				"image": "../img/logo.png"
        },
            {
                "name": "Pure con Carne",
                "value": 16,
   				"image": "../img/logo.png"             
 
        }];



data = data.sort(function (a, b) {
            return d3.ascending(a.value, b.value);
        })
var margin = {
            top: 15,
            right: 25,
            bottom: 15,
            left: 200
 };

  var width = 1050 - margin.left - margin.right,
            height = 500 - margin.top - margin.bottom;


 var svg = d3.select("#graphic").append("svg")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var x = d3.scale.linear()
            .range([0, width])
            .domain([0, d3.max(data, function (d) {
                return d.value;
            })]);

var y = d3.scale.ordinal()
            .rangeRoundBands([height, 0], .1)
            .domain(data.map(function (d) {
                return d.name;
            }));

var yAxis = d3.svg.axis()
            .scale(y)
            //no tick marks
           // .tickSize(0) 
            .orient("left");

 var gy = svg.append("g")
            .attr("class", "y axis")
            .call(yAxis)
            
 var bars = svg.selectAll(".bar")
            .data(data)
            .enter()
            .append("g")

        //append rects
bars.append("rect")
            .attr("class", "bar")
            .attr("y", function (d) {
                return y(d.name);
            })
            .attr("height", y.rangeBand())
            .attr("x", 0)
            .attr("width", function (d) {
                return x(d.value);
            });

        //add a value label to the right of each bar
bars.append("text")
            .attr("class", "label")
            //y position of the label is halfway down the bar
            .attr("y", function (d) {
                return y(d.name) + y.rangeBand() / 2 + 4;
            })
            //x position is 3 pixels to the right of the bar
            .attr("x", function (d) {
                return x(d.value) + 3;
            })
            .text(function (d) {
                return d.value;
            });



function arreglo(){
    var barras = jQuery(".bar")
    var i;
    var color = ["#96ceb4","#ff6f69","#ffcc5c","#ffeead","#88d8b0"]
    for(i=0; i<barras.length; i++){
        barras[i].style.fill = color[i];
    }
}




//chartist
/*
var data2 = {
  labels: ['Jan', 'Feb', 'Mar', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    series: [
    [5, 4, 3, 7, 5, 10, 3, 4, 8, 10, 6, 8],
    [3, 2, 9, 5, 4, 6, 4, 6, 7, 8, 7, 4]
  ]
};

var options = {
  seriesBarDistance: 15
};

var responsiveOptions = [
  ['screen and (min-width: 641px) and (max-width: 1024px)', {
    seriesBarDistance: 10,
    axisX: {
      labelInterpolationFnc: function (value) {
        return value;
      }
    }
  }],
  ['screen and (max-width: 640px)', {
    seriesBarDistance: 5,
    axisX: {
      labelInterpolationFnc: function (value) {
        return value[0];
      }
    }
  }]
];

new Chartist.Bar('.ct-chart', data2, options, responsiveOptions);*/
/*
$("#id_username").change(function () {
      var username = $(this).val();

      $.ajax({
        url: '/ajax/validate_username/',
        data: {
          'username': username
        },
        dataType: 'json',
        success: function (data) {
          if (data.is_taken) {
            alert("A user with this username already exists.");
          }
        }
      });

    });*/



platos=[]

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

    
        