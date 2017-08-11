$( document ).ready(function() {
     $('[name^=rating]').change(function(){
        value = this.getAttribute("value");
        platoId = this.parentElement.getAttribute("id_p");
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
