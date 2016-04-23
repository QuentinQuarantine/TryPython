var python_console_rest_api = (function() {


    // private
    var _getCsrfToken = function(name) {
        var csrf_element = document.getElementsByName(name)[0];
        return csrf_element.value;
    };

    var _create_ajax = function(params, url, success, error){
        if (!params){
            params  = {};
        }
        params.csrfmiddlewaretoken = _getCsrfToken('csrfmiddlewaretoken');
        api.jquery.ajax({
            url: url,
            dataType: 'json',
            type: 'POST',
            data: params,
            success: success,
            error: error
        });
    };

    // public
    var api = {};

    api.init = function(jquery) {
        csrftoken = _getCsrfToken('csrfmiddlewaretoken');
        api.jquery = jquery;
        api.jquery.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });
    };

    api.sendPythonExpression = function(expression, success, error) {
        _create_ajax({'toEval': expression}, '/eval', success, error);
    };

    api.getStep = function(step, callback){
        _create_ajax({'step': step}, '/get_step', callback);
    };

    return api;
})();
