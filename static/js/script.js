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