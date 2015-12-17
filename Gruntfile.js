module.exports = function(grunt) {
  grunt.initConfig({
    jasmine : {
      // Your project's source files
      src : [
        'TryPython/try_python_tutorial/static/js/lib/jquery.min.js',
        'TryPython/try_python_tutorial/static/js/lib/jquery.console.js',
        'TryPython/try_python_tutorial/static/js/src/*.js',
        ],
      options : {
        specs : [
          'TryPython/try_python_tutorial/static/js/test/specHelper.js',
          'TryPython/try_python_tutorial/static/js/test/*.js'
          ],
      }
    },
    jshint: {
      all: [
        'TryPython/try_python_tutorial/static/js/src/*.js',
        'TryPython/try_python_tutorial/static/js/test/*.js'
        ]
    }
  });

  grunt.loadNpmTasks('grunt-contrib-jasmine');
  grunt.loadNpmTasks('grunt-contrib-jshint');

  // Default task.
  grunt.registerTask('test', ['jasmine', 'jshint']);
};