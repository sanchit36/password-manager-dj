from django.urls import path
from .views import pass_list_view, add_site, delete_site, edit_site


urlpatterns = [
    path('', pass_list_view, name="index"),
    path('add-site', add_site, name="add_site"),
    path('delete-site/<int:pk>', delete_site, name="delete_site"),
    path('edit-site/<int:pk>', edit_site, name="edit_site"),
]
