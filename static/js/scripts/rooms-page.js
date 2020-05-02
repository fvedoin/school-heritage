$(document).ready(function () {

    setInitialView();

    //Input for searching
    const searchField = $('#dt-search');

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