function ModalForm() {
    this.urlBase = "";
    this.name = "";
    this.pk = null;
    this.defaults = {};
    this.excluded = new Set();

    this.setFieldValues = function(onSuccess) {
        // get form field values by form name & pk
        var url = this.urlBase + "/" + this.name + (this.pk ? "/" + this.pk : "");
        var mf = this;

        $.get(url, function(data) {
            var fields = JSON.parse(data);
    
            // inject default fields
            for (var field in mf.defaults) {
                field_id = mf.name + "_" + field;
                fields[field_id] = mf.defaults[field];
            }

            // remove excluded fields
            mf.excluded.forEach(function(field) {
                field_id = mf.name + "_" + field;
                delete fields[field_id];
            });
    
            // set field values
            for (var field in fields) {
                var value = fields[field];
                var field_id = '#' + field;
                var input = $(field_id);
    
                var isCheckbox = input.attr('type') == "checkbox";
                var isMultiple = input.attr('multiple') == "multiple";
    
                if (isCheckbox) {
                    input.prop('checked', value);
                } else if (isMultiple) {
                    $.each(value, function(i, v) {
                        var selector = field_id + ' option[value="' + v + '"]';
                        $(selector).prop("selected", true);
                    });
                } else {
                    input.val(value);
                }
            }

            onSuccess();
        });
    }

    this.displayModal = function(invalid = false) {
        var modal = $('#mf-' + this.name );
        
        // set action label
        var actionLabel = this.pk ? "Edit" : "Add";
        modal.find('.mf-action-label').html(actionLabel);
    
        // set hidden pk field
        modal.find('input[name="mf-pk"]').val(this.pk);

        if (invalid) {
            // display warning on modal close
            function displayWarning(e) {
                var close = confirm("Form data has not been saved... are you sure you want to close this form?");
                if (close) {
                    modal.off('hide.bs.modal', displayWarning);
                } else {
                    e.preventDefault();
                }
            }

            modal.on('hide.bs.modal', displayWarning);
        } else {
            // clear previous error state
            $('.mf-error').remove();
        }
    
        // display modal
        modal.modal('show');
    }
}

$(document).ready(function() {
    var urlBase = $('#mf-url-base').val();
    var invalid = $('#mf-invalid');

    // display modal if submitted form is invalid
    if (invalid.length) {
        var mf = new ModalForm();
        mf.name = invalid.data('mf_name');
        mf.pk = invalid.data('mf_pk');
        mf.displayModal(true);
    }

    // setup and display modal form
    $('body').on('click', '.mf-btn', function() {
        var btn = $(this);

        var mf = new ModalForm();
        mf.urlBase = urlBase;
        mf.name = btn.data('mf_name');
        mf.pk = btn.data('mf_pk');

        // default values
        var defaults = btn.data('mf_defaults');
        if (defaults) {
            mf.defaults = btn.data('mf_defaults');
        }

        // excluded values
        var excluded = btn.data('mf_excluded');
        if (excluded) {
            mf.excluded = new Set(excluded);
        }

        mf.setFieldValues(function() {
            mf.displayModal();
        });
    });
});
