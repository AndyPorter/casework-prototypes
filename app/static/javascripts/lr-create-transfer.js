(function($) {
  "use strict";

  $(function() {
    var $restrictions = $(".restriction-panel"),
        $uploads = $restrictions.find(".supporting-uploads").hide();

    $restrictions.each(function(index, el) {
      $(el).find("[name='evidence-provided']").on('change', function() {
        if( $(this).val() === "confirm" ) {
          $uploads.show();
        } else {
          $uploads.hide();
        }
      });
    });
  });

}(jQuery));
