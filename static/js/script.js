$(".column" ).hover( showControls, hideControls);

$(".fas").click(function(){
    let curScroll = $('.column').scrollLeft();

    if($(this).hasClass("fa-angle-left")){
        $('.column').scrollLeft(curScroll - 50);
    } else{
        $('.column').scrollLeft(curScroll + 50);
    }
});

function showControls(){
    /* Add Arrows */
    if($(".fas.fa-angle-left").length == 0){
        $('.column').append('<i class="fas fa-angle-left"></i>');
        $('.column').append('<i class="fas fa-angle-right"></i>');
    };
}

function hideControls(){
    /* Remove Arrows */
    if($(".fas.fa-angle-left").length == 1){
        $('.fas.fa-angle-left').remove();
        $('.fas.fa-angle-right').remove();
    };
}