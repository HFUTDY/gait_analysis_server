(function() {
    $('#starttime').datepicker({
        onSelect: function(date) {
            $('#starttime').parent().find('.value').text(date);
            $('#timeform').submit();
        },
        dateFormat: 'yy-mm-dd'
    });
})();