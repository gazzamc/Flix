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
}, function(){
    $(this).find("i").css('display', 'none');
});

$('.delete-item-icon').click(function(){
    slug = $(this).siblings().find("img").attr("alt");
    $.get(location + slug, function() {
        location.reload();
    });
});