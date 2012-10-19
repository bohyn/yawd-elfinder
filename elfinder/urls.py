from django.conf import settings
from django.conf.urls.defaults import patterns, url, include
from views import ElfinderConnectorView

urlpatterns = patterns('',
    url(r'^yawd-connector/(?P<optionset>.+)/(?P<start_path>.+)/$', ElfinderConnectorView.as_view(), name='yawdElfinderConnectorView'),
)

if 'elfinder.tinymce' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^yawd-extras/', include('elfinder.tinymce.urls'))
    )
