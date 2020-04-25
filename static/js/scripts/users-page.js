$(".telefone").mask("(00) 0000-00009");
$(document).ready(function () {
    $('#btn-close-div-form-user').click(function () {
        $('#div-form-user').hide();
        $('#div-list-users').show();
    });
    $('#btn-show-div-form-user').click(function () {
        $('#div-form-user').show();
        $('.messages').hide();
        $('#div-list-users').hide();
    });
    var tableDt = $('#table-users').DataTable({
        sDom: 'lrtip',
        "pageLength": 10,
        "lengthChange": false,
        "info": true,
        "columnDefs": [
            {"orderable": false, "searchable": false, "targets": [5]},
            {"orderable": false, "targets": [2, 3, 4]}
        ]
    });
    var inputSearch = $('#inputSearch');

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
    $('.btn-delete-user').on('click', function (e) {
        e.preventDefault();
        $('#div-messages-delete-user').hide();
        var tr = $(this).parent().parent();
        $.get($(this).attr('href'), function (data) {
            if (data.success) {
                var html = '  <div class="alert alert-success alert-dismissible fade show" role="alert">' +
                    '                            <span>' + data.message + '</span>' +
                    '                            <button type="button" class="close" data-dismiss="alert" aria-label="Close">' +
                    '                                <span aria-hidden="true">&times;</span>' +
                    '                            </button>' +
                    '                        </div>';
                $('#div-messages-delete-user').html(html);
                $('#div-messages-delete-user').show('slow');
                tableDt.row(tr).remove().draw(false);
            }
        }, "json");
        return false;
    });
});