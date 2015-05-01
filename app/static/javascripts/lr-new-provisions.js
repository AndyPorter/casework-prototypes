(function($) {
  "use strict";

  $(function() {
    var target_provision = window.location.hash.substr(1).split('?')[0];

    if( $('#' + target_provision + '-text').length ) {
      var $details = $('details');
      $details.removeAttr('open');

      var test = $('#' + target_provision + '-text')
        .parents('details')
          .attr('open', 'true')
          .end()
        .focus();
    } else {
      $('#definitions-text').focus();
    }

  });

}(jQuery));