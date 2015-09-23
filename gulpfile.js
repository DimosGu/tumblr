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
  return gulp.src('./static/scss/*.scss')
        .pipe(sass({
          includePaths: ['styles'].concat(neat),
          onError: function (err) {
            notify().write(err);
          }
        }))
        .pipe(cssimport({
          extensions: ["css"]
        }))
        .pipe(gulp.dest('static/css/'));
});


gulp.task('minify-css', function() {
  return gulp.src('./static/css/*.css')
    .pipe(minifyCss())
    .pipe(gulp.dest('static/styles/css/'));
});


// gulp.task('build-js', function(){
//   var files = [ './static/js/admin.js', './static/js/public.js' ];
//   var b = browserify(files);
//   b.plugin('factor-bundle', { outputs: [ './static/js/bundle/admin.js', './bluehorse/static/js/bundle/public.js' ] });
//   b.bundle().pipe(fs.createWriteStream('./static/js/bundle/common.js'));
// });


// gulp.task('minify-js', function() {
//   return gulp.src('./bluehorse/static/js/bundle/*.js')
//     .pipe(uglify())
//     .pipe(gulp.dest('bluehorse/static/js/bundle/'));
// });


gulp.task('watch', function() {
  gulp.watch(['./static/styles/scss/*.scss', './static/styles/scss/**/*.scss'], ['build-sass']);
  // gulp.watch(['./static/js/**/*.js', '!./static/js/bundle/*.js'], ['build-js']);
});


gulp.task('default', ['build-sass', 'build-js', 'watch']);
gulp.task('build', ['build-sass', 'build-js']);
