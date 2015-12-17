describe("Python Console Tests", function() {
  var try_python_rest_api, jquery;
  beforeEach(function() {
    try_python_rest_api = {
    	_getCsrfToken: function(value) {
    		return "csrftoken";
    	},
    	init: function(jquery){

    	}
    };
    jquery = {
    	ready: function(){

    	},
    };

    spyOn(try_python_rest_api, '_getCsrfToken');
    spyOn(try_python_rest_api, 'init');
    spyOn(jquery, 'ready');
  });
  
  it("It should init the python console", function() {
    py_console.init($, try_python_rest_api);

    expect(py_console.jquery).toEqual($);
    expect(py_console.try_python_rest_api).toEqual(try_python_rest_api);
    expect(try_python_rest_api.init.calls.count(), 1);
    expect(jquery.ready.calls.count(), 1);
    expect(py_console.console).not.toBe(null);

  });

  it("py_console.console.promptLabel should be >>>", function(){
	py_console.init($, try_python_rest_api);

	expect(py_console.console.promptLabel).toEqual(">>> ");
  });

  it("py_console.console_options.continuedPromptLabel should be ...\\t", function(){
	py_console.init($, try_python_rest_api);

	expect(py_console.console_options.continuedPromptLabel).toEqual("...\t");
	
  });

  it("py_console.console_options.autofocus should be true", function(){
	py_console.init($, try_python_rest_api);

	expect(py_console.console_options.autofocus).toBe(true);
	
  });

  it("py_console.console_options.welcomeMessage should be 'Welcome to python interactive web console.'", function(){
	py_console.init($, try_python_rest_api);

	expect(py_console.console_options.welcomeMessage).toBe('Welcome to python interactive web console.');
	
  });

  it("py_console.console.commandHandle should return true", function(){
	py_console.init($, try_python_rest_api);

	expect(py_console.console_options.commandValidate('')).toBe(true);
	
  });

});