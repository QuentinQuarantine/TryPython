var py_console = (function() {

    var _get_last_statement = function(line) {
        var splited_line = line.split("\n");
        return splited_line[splited_line.length - 1];
    };

    var insert_space = function(quantity){
        var i = 0;
        if (!quantity){
            quantity = 4;
        }
        while(i < quantity){
            api.console.typer.consoleInsert(32); //inserts space
            i += 1;
        }
    };


    //public
    var api = {};
    api.statements = '';
    api.console_options = {};

    api.get_step = function(url){
        api.current_step = utils.parse_step_from_url(url);
        if (api.current_step){
          var tutorial_content_element = api.jquery(".tutorial-content");
          tutorial_content_element.empty().fadeOut("slow");
          api.rest_api.getStep(api.current_step, function(result){
             tutorial_content_element.append("<h2>" + result.title + "</h2>").fadeIn('slow');
             tutorial_content_element.append("<p>" + result.content + "</p>").fadeIn('slow');
          });
        }
    };

    api.console_options.commandValidate = function(line) {
        return true;
    };

    api.console_options.keyCodes = {
        9:  insert_space,
        18: insert_space
    };

    api.console_options.promptLabel = ">>> ";
    api.console_options.continuedPromptLabel = '...';
    api.console_options.autofocus = true;
    api.console_options.fadeOnReset = false;


    api.console_options.commandHandle = function(line, report) {
        if (!line){
            return '';
        }
        if (line.trim() === 'next'){
            api.get_step(window.location.href);
            api.console.reset();
            return;
        }
        if (api.console.continuedPrompt) {
            var last_statement = _get_last_statement(line);
            if (last_statement.trim()) {
                api.statements += '\n' + last_statement;
                return;
            }
        }
        if (line.endsWith(":")) {
            api.console.continuedPrompt = true;
            api.statements += _get_last_statement(line);
            return;
        } else {
            api.console.continuedPrompt = false;
        }
        if (api.statements) {
            line = api.statements + '\n';
            api.statements = "";
        }
        api.rest_api.sendPythonExpression(line, function(result) {
            var msgs = [];
            var out = result.out;
            var err = result.err;

            if (out.trim()) {
                out = out.split("\n");
                for (var l in out) {
                    line_out = out[l];
                    if (line_out.trim()) {
                        msgs.push({
                            msg: " " + line_out,
                            className: "jquery-console-message-value"
                        });
                    }
                }
                report(msgs);
            } else {
                report([{
                    msg: err.trim(),
                    className: "jquery-console-error"
                }]);
                return;
            }
        }, function(){
            alerts.show_error_alert(
                "Ops! Algo deu errado.", 
                "Se o problema persistir entre em contato conosco por" + 
                "<a href='https://github.com/IuryAlves/TryPython/issues/new' " + 
                "target='_blank'> aqui.</a>");
            report();
        });
    };

    api.init = function(jquery, python_console_rest_api, window, utils) {
        api.jquery = jquery;
        api.rest_api = python_console_rest_api;
        python_console_rest_api.init(jquery);

        api.current_step = 0;
        api.jquery(document).ready(function() {
            var console_element = api.jquery('<div class="console">');
            api.jquery('body').append(console_element);

            api.console = console_element.console(api.console_options);
            api.get_step(window.location.href);
        });
    };

    return api;
})();
