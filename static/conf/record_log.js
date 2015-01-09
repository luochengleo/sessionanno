/**
 *
 * Created by defaultstr on 1/10/15.
 */


var current_page_url = window.location.href;
var current_site = get_set(current_page_url);
var server_site = current_site;
var annotator_id = getCookie('annotatorID');


function get_set(url_str) {
    var ret = "127.0.0.1";
    var site_re = /http:\/\/([\w\.]+):8000\//;
    if (site_re.test(url_str)) {
        ret = RegExp.$1;
    }
    return ret;
}

function getCookie(c_name) {
    if (document.cookie.length > 0) {
        c_start = document.cookie.indexOf(c_name + "=")
        if (c_start != -1) {
            c_start = c_start + c_name.length + 1
            c_end = document.cookie.indexOf(";", c_start)
            if (c_end == -1) c_end = document.cookie.length
            return unescape(document.cookie.substring(c_start, c_end))
        }
    }
    return ""
}

$(function() {
   $("form").submit(function(e) {
       var score = $(this).find("input:text[name=score]").val();
       var student_id = $(this).find("input:hidden[name=studentID]").val();
       var task_id = $(this).find("input:hidden[name=task_id]").val();
       var log_url = "http://" + server_site + ":8000/RecordAnnoService/";
       var encode_str = 'annotatorID=' + annotator_id;
       encode_str += '\tstudentID=' + student_id;
       encode_str += '\ttask_id=' + task_id;
       encode_str += '\tscore=' + score + "\n";
       $.ajax({
            type: 'POST',
            url: log_url,
            data: {message: encode_str},
            async: false,
            complete: function (jqXHR, textStatus) {
                //alert(textStatus + "----" + jqXHR.status + "----" + jqXHR.readyState);
                //should we reset onbeforeunload here?
                console.log("synchronously flush annotations!")
            }
       });
       return false;
   });
});
