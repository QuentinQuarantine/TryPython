var python_console_rest_api = (function() {


    // private 
    var _getCsrfToken = function(name) {
        var csrf_element = document.getElementsByName(name)[0];
        return csrf_element.value;
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
        var data = {'toEval': expression};
        data.csrfmiddlewaretoken = _getCsrfToken('csrfmiddlewaretoken');
        api.jquery.ajax({
            url: '/eval',
            dataType: 'json',
            type: 'POST',
            data: data,
            success: callback
        });
    };

    return api;
})();