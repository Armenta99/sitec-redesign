$(window).on('load', function(){
    let syncSitecForm = $('.sync.sitec.form').form({

    }).api({
        on: 'submit',
        action: 'sync sitec',
        method: 'POST',
        beforeXHR: suiSetRequestHeaders,
        serializeForm: true,
        beforeSend: function(settings){
            return settings
        },
        onSuccess: function(){

        },
        onError: function(){

        }
    })
    let sitecModal = $('.sync.sitec.modal').modal({
        onApprove: function(){
            syncSitecForm.form('submit')
            return false
        }
    })
    let syncSitecButton = $('.sync.sitec.button')
    syncSitecButton.on('click', function(){
        sitecModal.modal('show')
    })



})