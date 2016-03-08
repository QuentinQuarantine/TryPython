describe("Python Console Tests", function() {
    var python_console_rest_api, jquery, window;
    beforeEach(function() {
        python_console_rest_api = {
            _getCsrfToken: function(value) {
                return "csrftoken";
            },
            init: function(jquery) {},
            sendPythonExpression: function(){},
            getStep: function(){}
        };
        jquery = {
            ready: function() {}
        };
        window = {
          location: {
            href: ''
          }
        };
        report = function(){};

        spyOn(python_console_rest_api, '_getCsrfToken');
        spyOn(python_console_rest_api, 'init');
        spyOn(python_console_rest_api, 'sendPythonExpression');
        spyOn(python_console_rest_api, 'getStep');
        spyOn(jquery, 'ready');
        spyOn(py_console, 'get_step').and.callThrough();
        spyOn(py_console, 'init').and.callThrough();
    });

    it("Should init the python console", function() {
        py_console.init($, python_console_rest_api, window, utils);
        spyOn(py_console.console, 'reset').and.callThrough();

        expect(py_console.jquery).toEqual($);
        expect(py_console.init).toHaveBeenCalledWith($, python_console_rest_api, window, utils);
        expect(py_console.rest_api).toEqual(python_console_rest_api);
        expect(python_console_rest_api.init.calls.count(), 1);
        expect(jquery.ready.calls.count(), 1);
        expect(py_console.console).not.toBe(null);
        expect(py_console.current_step).toBe(null);
    });

    it("Should get the first step on document.ready when /step/number in url", function(){
        var url = '/step/1';
        window.location.href  = url;
        py_console.init($, python_console_rest_api, window, utils);
        spyOn(py_console.console, 'reset').and.callThrough();
        expect(py_console.get_step).toHaveBeenCalledWith(url);
        expect(python_console_rest_api.getStep).toHaveBeenCalledWith('1', jasmine.any(Function));
        expect(py_console.current_step).toEqual('1');
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

    it("py_console.console_options.welcomeMessage should be undefined", function() {
        expect(py_console.console_options.welcomeMessage).toBe(undefined);
    });

    it("py_console.console.commandValidate with empty string should return true", function() {
        expect(py_console.console_options.commandValidate('')).toBe(true);
    });

    it("py_console.console.commandHandle with expression should send the expression to backend", function() {
        py_console.init($, python_console_rest_api, window, utils);
        spyOn(py_console.console, 'reset').and.callThrough();
        py_console.console_options.commandHandle('1+1', report);

        expect(python_console_rest_api.sendPythonExpression).toHaveBeenCalledWith('1+1', jasmine.any(Function));
    });

    it("py_console.console.commandHandle should insert \\n after :", function() {
        py_console.init($, python_console_rest_api, window, utils);
        spyOn(py_console.console, 'reset').and.callThrough();
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

    it("if the input is empty commandHandle should not be called", function(){
        expect(py_console.console_options.commandHandle('', report)).toEqual('');
        expect(python_console_rest_api.sendPythonExpression).not.toHaveBeenCalled();
    });

    it("py_console.console_options.commandHandle with 'next' should call get_step and clean the console", function(){
        py_console.init($, python_console_rest_api, window, utils);
        spyOn(py_console.console, 'reset').and.callThrough();
        py_console.console_options.commandHandle('next', report);

        expect(py_console.get_step).toHaveBeenCalled();
        expect(py_console.console.reset).toHaveBeenCalled();
        expect(python_console_rest_api.sendPythonExpression).not.toHaveBeenCalled();
    });
});
