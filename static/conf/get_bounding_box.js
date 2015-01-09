/**
 *
 * Created by defaultstr on 1/3/15.
 */
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

function get_result_bounding_box() {
    var message_list = $('div.rb').map(function (i, e) {
        var rect = e.getBoundingClientRect();
        return 'query='+currentQuery+'\tpage='+currentPageID+'\tleft='+rect.left
        +'\ttop='+rect.top+'\tright='+rect.right+'\tbottom='+rect.bottom;
    });
    var message = '';
    for (var i = 0; i < message_list.length; i++) {
        message += message_list[i] + '\n';
    }
    console.log(message);
    return message;
}



function get_character_bounding_box() {
    var message_list = $('span.character_bound').map(function (i, e) {
        var rect = e.getBoundingClientRect();
        var c = e.innerHTML;
        var p = e.parentNode;
        while (p != null) {
            var name = p.className;
            if (name == 'pt' || name == 'ft' || name == 'fb') {
                break;
            }
            p = p.parentNode;
        }
        return 'query='+currentQuery+'\tpage='+currentPageID+'\ttype='+p.className
        +'\tid='+ e.id + '\tcharacter='+ e.innerHTML
        +'\tleft='+rect.left+'\ttop='+rect.top+'\tright='+rect.right+'\tbottom='+rect.bottom;
    });
    var message = '';
    for (var i = 0; i < message_list.length; i++) {
        message += message_list[i] + '\n';
    }
    console.log(message);
    return message;
}

function send_message(encode_str) {
    var log_url = "http://" + server_site + ":8000/debugLogService/";
    $.ajax({
        type: 'POST',
        url: log_url,
        data: {message: encode_str},
        async: false,
        complete: function (jqXHR, textStatus) {
            console.log("synchronously flush message!")
        }
    });
}

$(function() {
   send_message(get_character_bounding_box());
});