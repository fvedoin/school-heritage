setInitialView();

//Input for searching
const searchField = $('#dt-search');

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

function getColumns() {
    if (countCols() === 4) {
        return [
            {'targets': 0, 'orderable': true},
            {'targets': 1, 'orderable': false},
            {'targets': 2, 'searchable': false, 'width': '120px', 'className': 'operation-column'},
            {'targets': 3, 'orderable': false, 'searchable': false, 'width': '73px', 'className': 'operation-column'}
        ];
    } else {
        return [
            {'targets': 0, 'orderable': true},
            {'targets': 1, 'orderable': false},
            {'targets': 2, 'searchable': false, 'width': '120px', 'className': 'operation-column'}
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
}

//Executes the search on key up
searchField.on('keyup', function () {
    search();
});