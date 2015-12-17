module.exports = function(grunt) {
  grunt.initConfig({
    jasmine : {
      // Your project's source files
      src : [
        'TryPython/try_python_tutorial/static/js/jquery.min.js',
        'TryPython/try_python_tutorial/static/js/*.js',
        ],
      options : {
        specs : [
          'TryPython/try_python_tutorial/static/js/tests/specHelper.js',
          'TryPython/try_python_tutorial/static/js/tests/*.js'
          ],
      }
    }
  });

  // Register tasks.
  grunt.loadNpmTasks('grunt-contrib-jasmine');

  // Default task.
  grunt.registerTask('default', 'jasmine');
};