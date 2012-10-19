# -*- coding: utf-8 -*-
from django.core.exceptions import ImproperlyConfigured
from django.views.generic.base import TemplateView
from elfinder.conf import settings as ls


class TinyMCEScriptView(TemplateView):
    """
    View rendering template with TinyMCE filebrowser JavaScript function.
    """
    template_name = 'elfinder_tinymce_filebrowser_script.js'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context, mimetype='text/javascript')


# class TinyMCEDialogView(TemplateView):
#     """
#     View rendering Elfinder with TinyMCE popup bindings.
#     """
#     template_name = 'elfinder_tinymce_filebrowser_dialog.html'

#     def get_context_data(self, **kwargs):
#         tinymce_popup_js = ls.ELFINDER_TINYMCE_PATH_TO_POPUP_JS
#         if callable(tinymce_popup_js):
#             tinymce_popup_js = tinymce_popup_js()
#         kwargs['TINYMCE_POPUP_JS'] = tinymce_popup_js
#         return super(TinyMCEDialogView, self).get_context_data(**kwargs)
