/**
 *
 * Created by defaultstr on 11/28/14.
 */

if (studentID == "") {
    studentID = "0";
}

var current_page_url = window.location.href;
var current_site = get_set(current_page_url);
var server_site = current_site;


function get_set(url_str) {
    var ret = "127.0.0.1";
    var site_re = /http:\/\/([\w\.]+):8000\//;
    if (site_re.test(url_str)) {
        ret = RegExp.$1;
    }
    return ret;
}

$(function () {
    if ($("#session_annotation")) {
        $("#session_annotation").raty('set', {number: 5, starOn: "/static/conf/img/star-on.png", starOff: "/static/conf/img/star-off.png"});
    }
});

function session_over_button_on_click() {
    var score = $("#session_annotation").raty('score');
    var message = "";
    var client_time = (new Date()).getTime();
    message += "TIMESTAMP=" + client_time;
    message += "\tUSER=" + studentID;
    message += "\tTASK=" + currentTaskID;
    message += "\tACTION=SESSION_ANNOTATION";
    message += "\tINFO:";
    message += "\tscore="  + score + "\n"
    if (confirm("ok?")) {
        var encode_str = message;
        var log_url = "http://" + server_site + ":8000/SessionAnnoService/";
        $.ajax({
            type: 'POST',
            url: log_url,
            data: {message: encode_str},
            async: false,
            complete: function (jqXHR, textStatus) {
                //alert(textStatus + "----" + jqXHR.status + "----" + jqXHR.readyState);
                //should we reset onbeforeunload here?
                console.log("synchronously flush mouse log!")
            }
        });
        location.href = "/tasks/" + studentID + "/";
    }
}

function over_button_on_click() {
    var result_ids = $(".rb").map(function (i, e) {return e.id;});
    var result_urls = $(".rb h3 a").map(function (i, e) {return e.href;});
    var scores = $(".utility_annotation input").map(function (i, e) {return e.value;});
    var message = "";
    var client_time = (new Date()).getTime();
    for (var i = 0; i < result_ids.length; i++) {
        message += "TIMESTAMP=" + client_time;
        message += "\tUSER=" + studentID;
        message += "\tTASK=" + currentTaskID;
        message += "\tQUERY=" + currentQuery;
        message += "\tACTION=ANNOTATION";
        message += "\tINFO:";
        message += "\tid=" + result_ids[i];
        message += "\tsrc=" + result_urls[i];
        message += "\tscore=" + scores[i];
        message += "\n";
    }
    if (confirm("ok?")) {
        var encode_str = message;
        var log_url = "http://" + server_site + ":8000/AnnoService/";
        $.ajax({
            type: 'POST',
            url: log_url,
            data: {message: encode_str},
            async: false,
            complete: function (jqXHR, textStatus) {
                //alert(textStatus + "----" + jqXHR.status + "----" + jqXHR.readyState);
                //should we reset onbeforeunload here?
                console.log("synchronously flush mouse log!")
            }
        });
        window.close();
    }
}
