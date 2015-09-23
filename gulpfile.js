var gulp = require('gulp')
  , minifyCss = require('gulp-minify-css')
  , browserify = require('browserify')
  , fs = require('fs')
  , sass = require('gulp-sass')
  , uglify = require('gulp-uglify')
  , neat = require('node-neat').includePaths
  , notify = require("gulp-notify")
  , cssimport = require("gulp-cssimport")
;


// sass task
gulp.task('build-sass', function () {
  return gulp.src('./bluehorse/static/styles/scss/*.scss')
        .pipe(sass({
          includePaths: ['styles'].concat(neat),
          onError: function (err) {
            notify().write(err);
          }
        }))
        .pipe(cssimport({
          extensions: ["css"]
        }))
        .pipe(gulp.dest('bluehorse/static/styles/css/'));
});


gulp.task('minify-css', function() {
  return gulp.src('./bluehorse/static/styles/css/*.css')
    .pipe(minifyCss())
    .pipe(gulp.dest('bluehorse/static/styles/css/'));
});


gulp.task('build-js', function(){
  var files = [ './bluehorse/static/js/admin.js', './bluehorse/static/js/public.js' ];
  var b = browserify(files);
  b.plugin('factor-bundle', { outputs: [ './bluehorse/static/js/bundle/admin.js', './bluehorse/static/js/bundle/public.js' ] });
  b.bundle().pipe(fs.createWriteStream('./bluehorse/static/js/bundle/common.js'));
});


gulp.task('minify-js', function() {
  return gulp.src('./bluehorse/static/js/bundle/*.js')
    .pipe(uglify())
    .pipe(gulp.dest('bluehorse/static/js/bundle/'));
});


gulp.task('watch', function() {
  gulp.watch(['./bluehorse/static/styles/scss/*.scss', './bluehorse/static/styles/scss/**/*.scss'], ['build-sass']);
  gulp.watch(['./bluehorse/static/js/**/*.js', '!./bluehorse/static/js/bundle/*.js'], ['build-js']);
});


gulp.task('default', ['build-sass', 'build-js', 'watch']);
gulp.task('build', ['build-sass', 'build-js']);
