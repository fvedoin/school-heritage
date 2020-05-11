setInitialView();

$(".telefone").mask("(00) 0000-00009");

var tableDt = $('#dt').DataTable({
    sDom: 'lrtip',
    "pageLength": 10,
    'autoWidth': false,
    "lengthChange": false,
    "info": true,
    "columnDefs": [
        {"orderable": false, "searchable": false, "targets": 5, 'width': '73px'},
        {"orderable": false, "targets": [2, 3, 4]}
    ]
});

const inputSearch = $('#inputSearch');

function restartSearch() {
    tableDt.search(inputSearch.val()).columns().search('').draw();
}

function search() {
    restartSearch();
    var valueActive = $("#inputActive").val();
    if (valueActive != "") {
        tableDt.columns(4).search(valueActive).draw();
    }
    var valueRole = $("#inputRole").val();
    if (valueRole != "") {
        tableDt.columns(2).search(valueRole).draw();
    }
    var textSearch = inputSearch.val();
    if (textSearch != "") {
        tableDt.search(textSearch).draw();
    }

    if (valueRole == "" && valueActive == "" && textSearch == "") {
        restartSearch();
    }
}

$('#inputRole').change(function () {
    search();
});
$('#inputActive').change(function () {
    search();
});
inputSearch.on('keyup', function () {
    search();
});