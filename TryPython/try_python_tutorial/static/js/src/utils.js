if (!String.hasOwnProperty('endsWith')){
	String.prototype.endsWith = function(str){
		return this.match(str + "$") == str;
	};
}