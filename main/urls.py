from django.urls import path
from . import views
urlpatterns = [
    path('users_dashboard/', views.users_dashboard, name='users_dashboard'),
#===========================================================================
    path('upload_file/', views.upload_file, name='upload_file'),
    path('test/', views.test_url, name='test_url'),
    path('file/<pk>/delete', views.delete_file, name='delete_file'),
    path('image/<pk>/delete', views.delete_image, name='delete_image'),



#===========================================================================

]