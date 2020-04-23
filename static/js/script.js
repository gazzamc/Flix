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

$('.result-box').hover(function(){
    $(this).find("i").css('display', 'inline-flex');
    $(this).find("a").find("img").css('opacity', '0.6');
}, function(){
    $(this).find("i").css('display', 'none');
    $(this).find("a").find("img").css('opacity', '');
});

$('.delete-item-icon').click(function(){
    let baseUrl = window.location.protocol + "//" + window.location.host;
    let fullUrl = baseUrl + "/content/watch-list/";

    slug = $(this).siblings().find("img").attr("alt");

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