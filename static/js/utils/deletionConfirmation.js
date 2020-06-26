$(".exclusion-form").click(function (e) {
    e.preventDefault();
    const currentForm = this;
    bootbox.confirm({
        title: 'Confirmação de exclusão!',
        message: 'Você realmente deseja excluir este registro?',
        buttons: {
            cancel: {
                label: '<i class="fa fa-times"></i> Não'
            },
            confirm: {
                label: '<i class="fa fa-check"></i> Sim'
            }
        },
        callback: function (confirmed) {
            confirmed && currentForm.submit();
        }
    });
});