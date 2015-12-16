var ajax = (function(){

    var api = {};

    var getCsrfToken = function(name){
        var csrf_element = document.getElementsByName(name)[0];
        return csrf_element.value;
    };


    api.initAjax = function(jquery){
        csrftoken = getCsrfToken('csrfmiddlewaretoken');

        jquery.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });
    };

    api.ajax = function(jquery, url, data, callback){
        data.csrfmiddlewaretoken = getCsrfToken('csrfmiddlewaretoken');
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