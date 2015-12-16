var ajax = (function(){

    var api = {};

    api.getCookie = function(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    };

    api.initAjax = function(jquery){
        csrftoken = api.getCookie('csrftoken');

        jquery.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });
    };

    api.ajax = function(jquery, url, data, callback){
        data.csrfmiddlewaretoken = api.getCookie('csrftoken');
        jquery.ajax({
        url: url,
        dataType: 'json',
        type: 'POST',
        data: data,
        success: callback
      });
    };

    return api;
})();