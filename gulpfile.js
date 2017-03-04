// requirements

var gulp = require('gulp');
var gulpBrowser = require("gulp-browser");
var reactify = require('reactify');
var del = require('del');
var size = require('gulp-size');


// tasks

gulp.task('transform', function () {
  var stream = gulp.src('./dmft_search/static/scripts/jsx/*.js')
    .pipe(gulpBrowser.browserify({transform: ['reactify']}))
    .pipe(gulp.dest('./dmft_search/static/scripts/js/'))
    .pipe(size());
  return stream;
});

gulp.task('del', function () {
  return del(['./dmft_search/static/scripts/js']);
});

gulp.task('default', ['del'], function () {
  gulp.start('transform');
  gulp.watch('./dmft_search/static/scripts/jsx/*.js', ['transform']);
});