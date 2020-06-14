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
    if (countCols() === 7) {
        return [
            {'targets': 0, 'orderable': false, 'searchable': false},
            {'targets': [1,2,3,4], 'orderable': true},
            {'targets': 5, 'orderable': false, 'searchable': false, 'width': '103px', 'className': 'operation-column'},
            {'targets': 6, 'searchable': true, 'visible': false}
        ];
    } else {
        return [
            {'targets': 0, 'orderable': false, 'searchable': false},
            {'targets': [1,2,3], 'orderable': true},
            {'targets': 4, 'searchable': true, 'visible': false}
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
    if (valueStatus != "") {
        if (countCols() === 6) {
            dt.columns(6).search(valueStatus).draw();
        }else{
            dt.columns(4).search(valueStatus).draw();
        }
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
