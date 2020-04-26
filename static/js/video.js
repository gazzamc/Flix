/* Retrieve Video timestamp and update db */
var videoCheck;

$( document ).ready(function() {
    startVideoCheck();
});

function startVideoCheck(){
    videoCheck = setInterval(addVideoToWatching, 10000);
}

function addVideoToWatching(){
    let fullUrl = baseUrl + "/content/watching/";

    /* Get Slug */
    path = window.location.pathname
    slug = path.split('/')[2]

    video = document.getElementById("video-content");
    duration = Math.round(video.duration);
    currTime = Math.round(video.currentTime);

    /* If current time is greater than 5sec
        Update db entry with time. */
    if((duration - currTime) < 15){
        let url = baseUrl + "/content/watched/" + slug;

        $.get(url, function() {
            /* Do nothing */
        });
    }else if(currTime > 5){
        let url = baseUrl + "/content/watching/" + slug + "?t=" + currTime + "&d=" + duration;

        /* Call View */
        $.get(url , function() {
            /* Do nothing */
        });
    }
}
