var python_console_rest_api = (function() {


    // private 
    var _getCsrfToken = function(name) {
        var csrf_element = document.getElementsByName(name)[0];
        return csrf_element.value;
    };

    var _build_json_ajax_call = function(params, url, callback){
        if (!params){
            params  = {};
        }
        params.csrfmiddlewaretoken = _getCsrfToken('csrfmiddlewaretoken');
        api.jquery.ajax({
            url: url,
            dataType: 'json',
            type: 'POST',
            data: params,
            success: callback
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

    api.sendPythonExpression = function(expression, callback) {
        _build_json_ajax_call({'toEval': expression}, '/eval', callback);
    };

    api.getStep = function(step, callback){
        _build_json_ajax_call({'step': step}, '/step', callback);
    };

    return api;
})();