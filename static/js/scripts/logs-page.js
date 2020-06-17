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
    'order': [[2, "desc"]],
    'columnDefs': [
        {'targets': [0, 2], 'orderable': true},
        {'targets': 2, 'type': 'num'},
        {'targets': 1, 'orderable': false},
        {'targets': 3, 'orderable': false, 'searchable': false, 'width': '53px', 'className': 'operation-column'}
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
