$(document).ready(function () {

    //Input for searching
    const searchField = $('#dt-search');
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

    //DataTable configuration
    const dt = $('#dt').DataTable({
        sDom: 'lrtip',
        'pageLength': 10,
        'lengthChange': false,
        'autoWidth': false,
        'info': true,
        'columnDefs': [
            { 'targets': 0, 'orderable': true },
            { 'targets': 1, 'orderable': false, 'searchable': false, 'width': '73px', 'className': 'operation-column' }
        ]
    });

    //Clean the filters
    function restartSearch() {
        dt.search(searchField.val()).columns().search('').draw();
    }

    //Looks for the match register on DataTable
    function search() {
        restartSearch();
        if (searchField.val()) {
            dt.search(searchField.val()).draw();
        }
    }

    //Executes the search on key up
    searchField.on('keyup', function () {
        search();
    });

});