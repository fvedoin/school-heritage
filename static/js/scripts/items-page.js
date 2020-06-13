setInitialView();

//Input for searching
const searchField = $('#dt-search');
const searchSelect = $('#dt-select-search');

//Counts the number of columns on items table
function countCols() {
    var colCount = 0;
    $('tr:nth-child(1) td').each(function () {
        if ($(this).attr('colspan')) {
            colCount += +$(this).attr('colspan');
        } else {
            colCount++;
        }
    });
    return colCount;
}

//Returns the columnDefs configuration depending on the number of columns
function getColumns() {
    if (countCols() === 4) {
        return [
            {'targets': 0, 'orderable': true},
            {'targets': 1, 'orderable': false},
            {'targets': 2, 'orderable': false, 'width': '120px', 'className': 'operation-column'},
            {'targets': 3, 'orderable': false, 'searchable': false, 'width': '73px', 'className': 'operation-column'}
        ];
    } else {
        return [
            {'targets': 0, 'orderable': true},
            {'targets': 1, 'orderable': false},
            {'targets': 2, 'orderable': false, 'width': '120px', 'className': 'operation-column'}
        ];
    }
}

//DataTable configuration
const dt = $('#dt').DataTable({
    sDom: 'lrtip',
    'pageLength': 10,
    'lengthChange': false,
    'autoWidth': false,
    'info': true,
    'columnDefs': getColumns()
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
    if (searchSelect.val()) {
        dt.columns(2).search(searchSelect.val()).draw();
    }
}

//Executes the search on key up
searchField.on('keyup', function () {
    search();
});

searchSelect.on('change', function () {
    search();
});