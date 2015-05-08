$(document).ready(function() {

        $('.summernote').summernote({
            airMode: true,
            airPopover: [
                ['color', ['color']],
                ['font', ['bold', 'underline', 'clear']],
                ['para', ['ul', 'paragraph']],
                ['table', ['table']],
                ['insert', ['link', 'picture']],
                ['style' , ['style']],
                ['fontname',['fontname']],
                ['fontsize', ['fontsize']]
              ]
        });



    });

/**
 * This function sets the summernote air's content with that of its respective element
 * @param {array} selectors_list - Array of arrays, where first element of nested
 *                                  array is the summernote div selector
 *                                  and the second is the respective input selector
 */
    function input_to_summernote(selectors_list){

    $.each(selectors_list, function(){
           $(this[0]).code($(this[1]).val());
        });
    }

/**
 * This function sets the inputs content with that of its respective summernote input
 * @param {array} selectors_list - Array of arrays, where first element of nested
 *                                  array is the summernote div selector
 *                                  and the second is the respective input selector
 */
    function summernote_to_input(selectors_list){

        $.each(selectors_list, function(){
           $(this[1]).val($(this[0]).code());
        });
    }

