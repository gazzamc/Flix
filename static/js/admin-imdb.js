$( document ).ready(function() {

    /* https://stackoverflow.com/questions/6153047/detect-changed-input-text-box */
    let timerid;
    $("input#id_imdb_link").on('input', function() {
    let value = $(this).val();
        if ($(this).data("lastval") != value) {

            $(this).data("lastval", value);
            clearTimeout(timerid);

            timerid = setTimeout(function() {
                splitValue = value.split("/");
                imdbId = '';

                for (i = 0; i < splitValue.length; i++) {
                    if(splitValue[i].substring(0,2) == "tt"){
                        imdbId = splitValue[i];
                    }
                }
                
                grab_data(imdbId);
            }, 1000);
        };
    });
});

function grab_data(imdbId){
    $.get("//omdbapi.com/?apikey=4b524edf&i=" + imdbId, function(data) {
        $("#id_title").val(data.Title);
        $("#id_description").val(data.Plot);

        conCatTags = data.Year + " ," + data.Director + " ," + data.Actors + " ," + data.Title;
        $("#id_tags").val(conCatTags);

        /* If multiple split, only checking first */
        genres = data.Genre.split(",");

        /* Select Genre if its there */
        options = $("#id_genre").children();
        options.each(function( index ) {
            if($(this).text().toLowerCase() == genres[0].toLowerCase()){
                $(this).attr('selected', true);
            }
        });
    }, "json" );
}