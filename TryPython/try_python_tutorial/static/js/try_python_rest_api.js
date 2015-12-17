var try_python_rest_api = (function(){


    // private 
    var _getCsrfToken = function(name){
        var csrf_element = document.getElementsByName(name)[0];
        return csrf_element.value;
    };

    // public 
    var api = {};

    api.init = function(jquery){
        csrftoken = _getCsrfToken('csrfmiddlewaretoken');

        jquery.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });
    };

    api.eval = function(jquery, url, data, callback){
        data.csrfmiddlewaretoken = _getCsrfToken('csrfmiddlewaretoken');
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