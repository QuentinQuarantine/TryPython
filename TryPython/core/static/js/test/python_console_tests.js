describe("Python Console Tests", function() {
    var python_console_rest_api, jquery;
    beforeEach(function() {
        python_console_rest_api = {
            _getCsrfToken: function(value) {
                return "csrftoken";
            },
            init: function(jquery) {},
            sendPythonExpression: function(){}
        };
        jquery = {
            ready: function() {

            },
        };

        spyOn(python_console_rest_api, '_getCsrfToken');
        spyOn(python_console_rest_api, 'init');
        spyOn(python_console_rest_api, 'sendPythonExpression');
        spyOn(jquery, 'ready');
        py_console.init($, python_console_rest_api);
        report = function(){};

    });

    it("It should init the python console", function() {

        expect(py_console.jquery).toEqual($);
        expect(py_console.rest_api).toEqual(python_console_rest_api);
        expect(python_console_rest_api.init.calls.count(), 1);
        expect(jquery.ready.calls.count(), 1);
        expect(py_console.console).not.toBe(null);

    });

    it("py_console.console.promptLabel should be >>>", function() {

        expect(py_console.console.promptLabel).toEqual(">>> ");
    });

    it("py_console.console_options.continuedPromptLabel should be ...", function() {

        expect(py_console.console_options.continuedPromptLabel).toEqual("...");

    });

    it("py_console.console_options.autofocus should be true", function() {

        expect(py_console.console_options.autofocus).toBe(true);

    });

    it("py_console.console_options.welcomeMessage should be 'Welcome to python interactive web console.'", function() {

        expect(py_console.console_options.welcomeMessage).toBe('Welcome to python interactive web console.');

    });

    it("py_console.console.commandValidate should return true", function() {

        expect(py_console.console_options.commandValidate('')).toBe(true);
    });

    it("py_console.console.commandHandle should send the expression to backend", function() {
    
        py_console.console_options.commandHandle('1+1', report);

        expect(python_console_rest_api.sendPythonExpression).toHaveBeenCalledWith('1+1', jasmine.any(Function));
    });

    it("py_console.console.commandHandle should insert \\n after :", function() {
    
        py_console.console_options.commandHandle('for x in (1, 2, 3):', report);

        expect(py_console.statements).toEqual('for x in (1, 2, 3):');
        expect(py_console.console.continuedPrompt).toBe(true);

        py_console.console_options.commandHandle('  print x', report);

        expect(py_console.statements).toEqual('for x in (1, 2, 3):\n  print x');
        expect(py_console.console.continuedPrompt).toBe(true);

        py_console.console_options.commandHandle('\n', report);

        expect(py_console.statements).toEqual('');
        expect(py_console.console.continuedPrompt).toBe(false);
        expect(python_console_rest_api.sendPythonExpression).toHaveBeenCalledWith('for x in (1, 2, 3):\n  print x\n', jasmine.any(Function));
    });

});