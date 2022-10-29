from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
urlpatterns = [
#===========================================================================
    path("list/", views.users_list, name="users_list"),
    path('<pk>/details/', views.user_details, name='user_details'),    

#===========================================================================
    path('profile/', views.user_profile, name='user_profile'),
    path("profile/update/", views.update_user_profile, name="update_user_profile"),
    path("profile/address/update/", views.update_user_address, name="update_user_address"),
    
    path("group/create/", views.create_user_group, name="create_user_group"),
    path("group/<pk>/update/", views.update_user_group, name="update_user_group"),
    

]


admin_urlpatterns = [
    path("admin/<pk>/change/", views.change_user, name="change_user"),
]

htmx_urlpatterns = [
  
]

ajax_urlpatterns = [
   
]

urlpatterns += admin_urlpatterns
urlpatterns += htmx_urlpatterns
urlpatterns += ajax_urlpatterns




