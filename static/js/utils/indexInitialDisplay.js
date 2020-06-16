function setInitialView() {
    //Initially display only the list section
    if ($('#form-create').find('ul.errorlist').length !== 0) {
        $('#list').hide();
    } else {
        $('#form-create').hide();
    }

    $('#close-form').click(function () {
        $('#form-create').hide();
        $('#list').show();
    });

    $('#show-form-create').click(function () {
        $('#form-create').show();
        $('#list').hide();
    });
}