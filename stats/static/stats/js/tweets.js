function getTimeSinceTweetPosted(tweet_date, element_id){

    var tweetDate = new Date(Date.parse(tweet_date));
    var nowDate = new Date();
    if (K.ie) {
        tweetDate = Date.parse(tdate.replace(/( \+)/, ' UTC$1'))
    }
    var displayTime = "";
    var diff = Math.floor((nowDate - tweetDate) / 1000);
    if (diff <= 1) {displayTime = "just now";}
    // else if (diff < 20) {displayTime = diff + " seconds ago";}
    // else if (diff < 40) {displayTime = "half a minute ago";}
    else if (diff < 60) {displayTime = "seconds ago";}
    else if (diff <= 90) {displayTime = "1 minute ago";}
    else if (diff <= 3540) {displayTime = Math.round(diff / 60) + " minutes ago";}
    else if (diff <= 5400) {displayTime = "1 hour ago";}
    else if (diff <= 86400) {displayTime = Math.round(diff / 3600) + " hours ago";}
    else if (diff <= 129600) {displayTime = "1 day ago";}
    else {displayTime = Math.round(diff / 86400) + " days ago";}
    // else if (diff < 604800) {displayTime = Math.round(diff / 86400) + " days ago";}
    // else if (diff <= 777600) {displayTime = "1 week ago";}
    // else {displayTime = "more than 1 week ago"}

    document.getElementById(element_id).textContent = displayTime;
}


var K = function () {
    var a = navigator.userAgent;
    return {
        ie: a.match(/MSIE\s([^;]*)/)
    }
}();
