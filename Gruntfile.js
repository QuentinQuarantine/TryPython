module.exports = function(grunt) {
  grunt.initConfig({
    jasmine : {
      // Your project's source files
      src : [
        'TryPython/core/static/js/dist/scripts.js',
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
    },
    concat: {
      dist: {
        src: ['bower_components/jquery/dist/jquery.min.js',
              'TryPython/core/static/js/lib/jquery.console.js',
              'TryPython/core/static/js/src/!(main).js', // main.js must be last file
              'TryPython/core/static/js/src/main.js'
            ],
        dest: 'TryPython/core/static/js/dist/scripts.js',
      },
    },
    watch: {
      options: {livereload: true},
      javascript: {
          files: ['TryPython/core/static/js/src/*.js'],
          tasks: ['concat']
      }
    }
  });

  grunt.loadNpmTasks('grunt-contrib-jasmine');
  grunt.loadNpmTasks('grunt-contrib-jshint');
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-watch');

  // Default task.
  grunt.registerTask('test', ['concat', 'jasmine', 'jshint']);
  grunt.registerTask('build', ['concat']);
  grunt.registerTask('default', ['concat', 'watch']);
};
