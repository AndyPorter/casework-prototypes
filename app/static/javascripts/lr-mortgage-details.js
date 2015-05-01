(function($) {
  "use strict";

  $(function() {
    var $m_form = $('.mortgage-details-form'),
        $inputs = $('input', $m_form).not('#nomortgagecheck'),
        $no_mortgage = $('#nomortgagecheck', $m_form);

    $no_mortgage.on('change', function(e) {
      if(this.checked) {
        $inputs.attr('disabled', true); // disable other inputs in form
        $m_form.addClass('no-mortgage'); // add class for styling
        switchAttrVals($m_form, 'action'); // switch form destination page
      } else {
        $inputs.removeAttr('disabled');
        $m_form.removeClass('no-mortgage');
        switchAttrVals($m_form, 'action');
      }
    });
  });

  function switchAttrVals($el, attr) {
    var oldVal = $el.attr(attr);
    $el.attr(attr, $el.data('alternative-' + attr));
    $el.data('alternative-' + attr, oldVal);
  }

}(jQuery));
