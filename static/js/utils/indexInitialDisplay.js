function setInitialView() {
//Initially display only the list section
    $('#form-create').hide();

    $('#close-form').click(function () {
        $('#form-create').hide();
        $('#list').show();
    });

    $('#show-form-create').click(function () {
        $('#form-create').show();
        $('#list').hide();
    });
}