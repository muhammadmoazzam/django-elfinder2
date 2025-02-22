from django.urls import path
from elfinder.views import index, connector_view
from elfinder.views_tinymce import tinymce_filebrowser_script_view, tinymce_filebrowser_dialog_view

urlpatterns = [
   path('<int:coll_id>/', index, name='elfinder_index'),
   path('connector/<int:coll_id>/', connector_view, name='elfinder_connector'),
   path('', index, name='elfinder_index'),
   path('connector/', connector_view, name='elfinder_connector'),
   path('tinymce/filebrowser-script/', tinymce_filebrowser_script_view, name='elfinder_tinymce_filebrowser_script'),
   path('tinymce/filebrowser-dialog/', tinymce_filebrowser_dialog_view, name='elfinder_tinymce_filebrowser_dialog'),
]