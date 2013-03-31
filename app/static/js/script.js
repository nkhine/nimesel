/* Author: Norman Khine

*/
$(document).ready(function(){
  language_complete = navigator.language.split("-");
  language = (language_complete[0]);
  console.log("Sprache (root): %s", language);
  var option = { resGetPath: '/locales/__lng__/__ns__.json', lng: language, debug: true};

  i18n.init(option, function() {
      // save to use translation function as resources are fetched
      $(".page-header").i18n();
  });
});
























