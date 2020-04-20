$( document ).ready(function() {
    /* If autoplay enabled focus video */
    if(!$("video").paused){
        vidInFocus(true);
    }

    /* Hides/Shows Controls when mouse hovers over column */
    $(".column").hover(showControls, hideControls);

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

    /* Changes opacity of video in jumbotron. */
    $("video, .fa-play").click(function(){
        vidInFocus(true);

        if($(this).hasClass("fa-play")){
            $("video").trigger("play");
        }
    });

    /* If video is playing pause on scroll */
    $(window).scroll(function(){
        /* Navigation Bar */
        if($(window).scrollTop() > 300){
            $("nav").removeClass("showNavBar");
            
            /* Featured Video */
            video = $("video");
            video.trigger('unload');
            vidInFocus(false);
        }else{
            $("nav").addClass("showNavBar");
        }

        /* PIP when scrolling */
        /* video.trigger('requestPictureInPicture'); */
    });
});
/**
 * 
 * @param {jQuery Object} item 
 * Checks if item is visible on screen
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
            /* Show arrows */
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
    /* Hide arrows */
    $('.fas.fa-angle-left').hide();
    $('.fas.fa-angle-right').hide();
}

/**
 * Change opacity of featured video.
 */
function vidInFocus(bool){
    if(bool){
        $("video#jumboVid").css("opacity", 1);
        hidePlayBtn(true);  
    } else{
        $("video#jumboVid").css("opacity", 0);
        $("video").trigger('pause');
        hidePlayBtn(false);
    }
}

/**
 * Change opacity of featured video.
 */
function hidePlayBtn(bool){
    if(bool){
        $(".fa-play").css("display", "none");    
    } else{
        $(".fa-play").css("display", "initial");
    }
}