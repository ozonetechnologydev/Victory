from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
urlpatterns = [
#===========================================================================
    path("admin/create/", views.create_teacher, name="create_teacher"),
    path("admin/list/", views.teachers_list, name="teachers_list"),
    path("admin/<pk>/update/", views.update_teachers, name="update_teachers"),
    path("admin/<pk>/delete/", views.delete_teachers, name="delete_teachers"),
#===========================================================================
    path("htmx/<pk>/delete/", views.htmx_delete_teachers, name="htmx_delete_teachers"),
    
    

]

