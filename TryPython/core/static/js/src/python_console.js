var py_console = (function() {

    // private
    var _statements = "";

    var _get_last_statement = function(line) {
        var splited_line = line.split("\n");
        return splited_line[splited_line.length - 1];
    };


    //public
    var api = {};
    api.console_options = {};

    api.console_options.commandValidate = function(line) {
        return true;
    };

    api.console_options.keyCodes = {
        9: function(){
            api.console.typer.consoleInsert(32); //inserts space
        },
        18: function(){
            api.console.typer.consoleInsert(32); //inserts space
        }
    };

    api.console_options.promptLabel = ">>> ";
    api.console_options.continuedPromptLabel = '...\t';

    api.console_options.commandHandle = function(line, report) {
        if (api.console.continuedPrompt) {
            var last_statement = _get_last_statement(line);
            if (last_statement.trim()) {
                if (!last_statement.endsWith(":")) {
                    _statements += '\n\t' + last_statement;
                } else if (last_statement.endsWith(":")) {
                    _statements += '\n' + last_statement;
                }
                return;
            }

        }
        if (line.endsWith(":")) {
            api.console.continuedPrompt = true;
            _statements += _get_last_statement(line);
            return;
        } else {
            api.console.continuedPrompt = false;
        }
        if (_statements) {
            line = _statements + '\n';
            _statements = "";
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
                    msg: err,
                    className: "jquery-console-error"
                }]);
                return;
            }
        });
    };
    api.console_options.welcomeMessage = 'Welcome to python interactive web console.';
    api.console_options.autofocus = true;

    api.init = function(jquery, python_console_rest_api) {
        api.jquery = jquery;
        api.rest_api = python_console_rest_api;
        python_console_rest_api.init(jquery);

        api.jquery(document).ready(function() {
            var console_element = api.jquery('<div class="console">');
            api.jquery('body').append(console_element);

            api.console = console_element.console(api.console_options);
        });
    };

    return api;
})();