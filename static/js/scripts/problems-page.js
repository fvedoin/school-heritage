setInitialView();

//Input for searching
const searchField = $('#dt-search');

//Counts the number of columns on problems table
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
    if (countCols() === 6) {
        return [
            {'targets': 0, 'orderable': false, 'searchable': true},
            {'targets': [1, 2, 3, 4], 'orderable': true},
            {'targets': 5, 'orderable': false, 'searchable': false, 'width': '103px', 'className': 'operation-column'}
        ];
    } else {
        return [
            {'targets': 0, 'orderable': false, 'searchable': true},
            {'targets': [1, 2, 3], 'orderable': true}
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
    'order': [[3, "desc"]],
    'columnDefs': getColumns()
});

//Clean the filters
function restartSearch() {
    dt.search(searchField.val()).columns().search('').draw();
}

//Looks for the match register on DataTable
function search() {
    restartSearch();
    var valueStatus = $("#inputStatus").val();
    if (valueStatus) {
        dt.columns(0).search("^" + valueStatus + "$", true, false, true).draw();
    }
    var textSearch = searchField.val();
    if (textSearch) {
        dt.search(textSearch).draw();
    }

    if (valueStatus == "" && textSearch == "") {
        restartSearch();
    }
}

$('#inputStatus').change(function () {
    search();
});
//Executes the search on key up
searchField.on('keyup', function () {
    search();
});
