from django.urls import path
from main.views import show_main, create_series, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, edit_series, delete_series, add_series_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-series', create_series, name='create_series'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-series/<int:id>', edit_series, name='edit_series'),
    path('delete/<int:id>', delete_series, name='delete_series'),
    path('create-series-ajax/', add_series_ajax, name='add_series_ajax'),
]