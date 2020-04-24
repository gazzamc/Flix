/* Global */
var baseUrl = window.location.protocol + "//" + window.location.host;

/* Profile */
/* modal actions */
$("button#cancel").click(function(){
    $("#cancel-modal").css("display", "block");
});

$("button#close, button#close-top").click(function(){
    $("#cancel-modal").css("display", "none");
});

/* Search */
$("#search-icon").click(function(){
    $("#searchbox").slideToggle("slow", function() {
  });
});

$('#searchbox, #fullsearchbox').keypress(function(event){
	if(event.which == '13'){
        search_term = $(this).val()
        window.location.href = "/search?q=" + search_term
	}
});

/* watch list */
$(".result-box").hover(function(){
    $(this).find("i").css('display', 'inline-flex');
    $(this).find("a").find("img").css('opacity', '0.6');

    if(window.location.pathname != "/"){
        $(this).find("a").find("img").addClass("img-big");
    } else{
        $(this).addClass("result-box-hover");
    }
    
}, function(){
    $(this).find("i").css('display', 'none');
    $(this).find("a").find("img").css('opacity', '');

    if(window.location.pathname != "/"){
        $(this).find("a").find("img").removeClass("img-big");
    } else{
        $(this).removeClass("result-box-hover");
    }
});

$(".delete-item-icon").click(function(){
    let fullUrl = baseUrl + "/content/watch-list/";
    let slug = $(this).siblings().find("img").attr("alt");

    /* Check if last item if so refresh */
    let count = $('.result-box').length

    /* if on watchlist page remove */
    if(location.pathname == "/content/watch-list/"){
        $(this).parent().remove();
    }

    $.get(fullUrl + slug, function() {
        if(count == 1){
            location.reload();
        }
    });

    /* Swap icons */
    if($(this).hasClass("fa-times-circle")){
        $(this).addClass("fa-plus");
        $(this).removeClass("fa-times-circle");
    } else{
        $(this).addClass("fa-times-circle");
        $(this).removeClass("fa-plus");
    }
});

/* Likes */
$(".fa-thumbs-up, .fa-thumbs-down").click(function(){
    let slug = $(this).siblings().find("img").attr("alt");

    if($(this).hasClass("fa-thumbs-up")){
        /* Add To Likes */
        if($(this).hasClass("shaded-icon")){
            $(this).removeClass("shaded-icon");
            $(this).siblings(".fa-thumbs-down").addClass("shaded-icon");
        } else{
            if($(this).siblings(".fa-thumbs-down").hasClass("shaded-icon")){
                $(this).siblings(".fa-thumbs-down").removeClass("shaded-icon");
            } else{
                $(this).siblings(".fa-thumbs-down").addClass("shaded-icon");
            }
        }

        $.get(baseUrl + "/content/like/" + slug, function() {
            /* show modal */
            $("#message-modal").show();
        });
    } else{
        /* Add To Dislikes */
        if($(this).hasClass("shaded-icon")){
            $(this).removeClass("shaded-icon");
            $(this).siblings(".fa-thumbs-up").addClass("shaded-icon");
        } else{
            if($(this).siblings(".fa-thumbs-up").hasClass("shaded-icon")){
                $(this).siblings(".fa-thumbs-up").removeClass("shaded-icon");
            } else{
                $(this).siblings(".fa-thumbs-up").addClass("shaded-icon");
            }
        }

        $.get(baseUrl + "/content/dislike/" + slug, function() {
            /* Add/Remove from like list */
        });
    }
});