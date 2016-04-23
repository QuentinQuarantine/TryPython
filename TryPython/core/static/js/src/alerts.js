var alerts = (function(jquery){
	var module = {};

	module.show_error_alert = function(message, sub_message){
		var template = '<div class="ui error message">' +
                       '<i onclick="alerts.close_alert()" class="close icon">' + 
                       '</i><div class="header">' +
                        message + '</div><p>' + sub_message + '</p></div>';
		jquery('body').prepend(template).fadeIn('slow');
	};

	module.close_alert = function(){
		var alert = jquery('.message');
		alert.fadeOut('slow', function(){
			$(this).remove();
		});
	};

	return module;
})($);
