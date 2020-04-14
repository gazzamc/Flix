$( document ).ready(function() {
    /* Hides/Shows Controls when mouse hovers over column */
    $(".column").hover( showControls, hideControls);

    /* Moves Items when clicking arrow buttons */
    $(".fas").click(function(){
        let id = $(this).parent().attr('id')
        let curScroll = $('#' + id + ".column").scrollLeft();

        if($(this).hasClass("fa-angle-left")){
            $('#' + id + ".column").scrollLeft(curScroll - 50);
        } else{
            $('#' + id + ".column").scrollLeft(curScroll + 50);
        }
    });
});

/**
 * 
 * @param {jQuery Object} item 
 * Checks if item is is visible om screen
 */
function isVisible(item){
    let result = false;
    let offset = item.offset();

    if(offset.left < window.innerWidth){
        result = true;
    }
    return result;
}

/**
 * Shows controls only when there is items
 * hidden.
 */
function showControls(){
    let id = $(this).attr("id");
    let curScroll = $("#" + id + ".column").scrollLeft();

    $("#" + id + ".column img").each(function(item){
        if(!isVisible($(this))){
            /* show Arrows */
            if(curScroll > 0){
                $('#' + id + ' .fas.fa-angle-left').show();
                $('#' + id + ' .fas.fa-angle-right').show();
            } else {
                $('#' + id + ' .fas.fa-angle-right').show();
            }
        } 
    });
}

/**
 * Hides controls.
 */
function hideControls(){
    /* hide Arrows */
    $('.fas.fa-angle-left').hide();
    $('.fas.fa-angle-right').hide();
}