$( document ).ready(function() {
    $(".column").hover( showControls, hideControls);

    $(".fas").click(function(){
        let id = $(this).parent().attr('id')
        let curScroll = $('#' + id + ".column").scrollLeft();
        console.log(id);

        if($(this).hasClass("fa-angle-left")){
            $('#' + id + ".column").scrollLeft(curScroll - 50);
        } else{
            $('#' + id + ".column").scrollLeft(curScroll + 50);
        }
    });
});

function showControls(){
    let column = $(this).attr("id");
    /* show Arrows */
    $('#' + column + ' .fas.fa-angle-left').show();
    $('#' + column + ' .fas.fa-angle-right').show();
}

function hideControls(){
    /* hide Arrows */
    $('.fas.fa-angle-left').hide();
    $('.fas.fa-angle-right').hide();
}