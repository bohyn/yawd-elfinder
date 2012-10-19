function elFinderBrowser(field_name, url, type, win) {

    if($('#elfinder').length == 0) {
        $('body').append($('<div/>').attr('id', 'elfinder'));
        $('#elfinder').elfinder({
            url: '{% url yawdElfinderConnectorView "default" "default" %}',
            getFileCallback: function(obj) {
                win.document.forms[0].elements[field_name].value = obj.url;
                $('#elfinder').dialog('close');
            }
        });
    } else {
        $('#elfinder').elfinder('open');
    }
    $('#elfinder').dialog({ width: 1000, modal: true, title: 'Files', zIndex: 400001 });
}
