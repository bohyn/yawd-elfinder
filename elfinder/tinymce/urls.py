from django.conf.urls.defaults import patterns, url
from views import TinyMCEScriptView

urlpatterns = patterns('',
    url(r'^tinymce-filebrowser-script/$', TinyMCEScriptView.as_view(), name='yawdElfinderTinyMCEScript'),
    # url(r'^tinymce-dialog/$', TinyMCEDialogView.as_view(), name='yawdElfinderTinyMCEDialog')
)
