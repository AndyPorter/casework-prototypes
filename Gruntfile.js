module.exports = function(grunt) {

  var globalConfig = {
    govuk_template: {
      css_dev: 'app/static/govuk-template/stylesheets/',
      js_dev: 'app/static/govuk-template/javascripts/',
      img_dev: 'app/static/govuk-template/images/'
    },
    scss: {
      dev: 'app/static/stylesheets/'
    }
  };

  // Project configuration.
  grunt.initConfig({

    globalConfig: globalConfig,

    pkg: grunt.file.readJSON('package.json'),

    jshint: {
      all: ['Gruntfile.js', 'app/static/javascripts/lr-*.js']
    },

    jsonlint: {
      protodata: {
        src: [ 'app/static/data/*.json' ]
      }
    },

    sass: {
      dev: {
        options: {
          style: 'expanded',
          loadPath: 'node_modules/govuk_frontend_toolkit/govuk_frontend_toolkit/stylesheets'
        },
        files: [{
          expand: true,
          cwd: '<%= globalConfig.scss.dev %>',
          src: ['*.scss'],
          dest: '<%= globalConfig.scss.dev %>',
          ext: '.css'
        }]
      }
    },

    watch: {
      css: {
        files: ['<%= globalConfig.scss.dev %>**/*.scss'],
        tasks: ['sass:dev'],
        options: {
          spawn: false,
        }
      }
    }

  });

  // Load the plugin that provides the "sass" task: https://github.com/gruntjs/grunt-contrib-sass
  grunt.loadNpmTasks('grunt-contrib-sass');

  // css-min task - used to minify straight css files (i.e. the govuk_template files): https://github.com/gruntjs/grunt-contrib-cssmin
  grunt.loadNpmTasks('grunt-contrib-cssmin');

  // copy task: https://github.com/gruntjs/grunt-contrib-copy
  grunt.loadNpmTasks('grunt-contrib-copy');

  // js uglify: https://github.com/gruntjs/grunt-contrib-uglify
  grunt.loadNpmTasks('grunt-contrib-uglify');

  // watch task. Does what it says on the tin: https://github.com/gruntjs/grunt-contrib-watch
  grunt.loadNpmTasks('grunt-contrib-watch');

  // js hint task: https://github.com/gruntjs/grunt-contrib-jshint
  grunt.loadNpmTasks('grunt-contrib-jshint');

  // json lint task: check json for syntax errors
  grunt.loadNpmTasks('grunt-jsonlint');

  // Register the various Grunt commands:

  // 1: Default task - watch for changes in landregistry elements, and serve the app
  grunt.registerTask('default', ['watch']);

  // 2: Build sass manually
  grunt.registerTask('build', ['sass:dev']);

};