//
// // document.write(document.getElementById('.team-logo').getAttribute('data-src'));
// // document.write("test");
// // var team_image = document.getElementById('team-logo');
// // document.write(team_image.id);
// //
// // //test = new Image();
// // //test.src = url("{% static 'images/knicks.jpg' %}")
// // document.write('<img src = "{% static \'images/knicks.jpg\' %}"');
// // team_image.src= url("{% static 'images/knicks.jpg' %}");
//
// function setTeamLogo(abbreviation, url) {
//     document.write(abbreviation);
//     document.write(static_url);
//     //var test = 'https://cdn.sstatic.net/stackexchange/img/logos/so/so-icon.png';
//     //var test = url('{% static "images/knicks.jpg" %}');
//     //var test = url("../../images/knicks.jpg");
//     //var test = "https://www.nba.com/.element/img/1.0/teamsites/logos/teamlogos_500x500/nyk.png";
//     var c = document.getElementById("myCanvas-" + abbreviation);
//     var ctx = c.getContext("2d");
//     var img = new Image();
//     img.onload = function () {
//         ctx.drawImage(img, 0, 0);
//     };
//     img.src = url;
//     // img.src= '{% static "images/knicks.jpg" %}';
//
//     //document.write(c.getAttribute('data-src'));
// }


function getBoxScoreURL(game_id, date, home_team_name, element_id){

    var yourElement = document.getElementById(element_id);
    var dateArray = date.split('-');
    var boxScoreURL = "https://www.basketball-reference.com/boxscores/" + dateArray[0] + dateArray[1] + dateArray[2] + "0" + home_team_name + ".html";
    //document.write(boxScoreURL);
    yourElement.setAttribute('href', boxScoreURL);
}


