( function( $ ) {
    //initialize Skrollr
    var s = skrollr.init({
        render: function(data){
            console.log(data.curTop);
        }
    });
})( jQuery);
