$( document ).ready(function() {
     $('[name^=rating]').change(function(){
        value = this.getAttribute("value");
        platoId = this.parentElement.getAttribute("id");
        console.log(value);
        console.log(this.parentElement);
        jQuery.ajax({
              url: "/FoodFinder/valorar",
              dataType: "json",
              data: { plato_id: platoId, valor: value },
              type: 'GET',
              error: function(XMLHttpRequest, textStatus, errorThrown){
                  console.log(errorThrown);
              }
          });
     });
});
