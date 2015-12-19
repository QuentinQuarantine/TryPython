module.exports = function(grunt) {
  grunt.initConfig({
    jasmine : {
      // Your project's source files
      src : [
        'TryPython/core/static/js/lib/jquery.min.js',
        'TryPython/core/static/js/lib/jquery.console.js',
        'TryPython/core/static/js/src/*.js',
        ],
      options : {
        specs : [
          'TryPython/core/static/js/test/specHelper.js',
          'TryPython/core/static/js/test/*.js'
          ],
      }
    },
    jshint: {
      all: [
        'TryPython/core/static/js/src/*.js',
        'TryPython/core/static/js/test/*.js'
        ]
    }
  });

  grunt.loadNpmTasks('grunt-contrib-jasmine');
  grunt.loadNpmTasks('grunt-contrib-jshint');

  // Default task.
  grunt.registerTask('test', ['jasmine', 'jshint']);
};