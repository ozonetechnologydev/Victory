from django.contrib.auth import views as auth_views
from django.urls import path

from accounts import views, views_ajax, views_htmx

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
#===========================================================================
#===========================================================================
    path("create/", views.create_user, name="create_user"),
    path("update/", views.update_user_account, name="update_user_account"),
    path("close/", views.close_user_account, name="close_user_account"),
    path("delete/", views.delete_user_account, name="delete_user_account"),
    path("delete_or_close/multiple/", views.multi_close_and_delete_user_account, name="multi_close_and_delete_user_account"),
    
    path('password/change/', views.change_password, name="change_password"),
#===========================================================================
#===========================================================================
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="accounts/authentication_reset_password.html"), name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/authentication_reset_password_done.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/authentication_reset_password_confirm.html"), name="password_reset_confirm"),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/authentication_reset_password_complete.html"), name="password_reset_complete"),
#===========================================================================
]

admin_urlpatterns = [
    path("admin/<pk>/delete/", views.delete_user, name="delete_user"),
    path('admin/password/change/', views.admin_change_password, name="admin_change_password"),
]

htmx_urlpatterns = [
    # path("htmx/create/", views_htmx.htmx_create_user, name="htmx_create_user"), 
    
    path("htmx/image/<pk>/set/profile/", views_htmx.htmx_set_profile_image, name="htmx_set_profile_image"), 
    path("htmx/image/<pk>/set/cover/", views_htmx.htmx_set_cover_image, name="htmx_set_cover_image"), 
    path("htmx/image/<pk>/delete/", views_htmx.htmx_delete_user_image, name="htmx_delete_user_image"), 
]

ajax_urlpatterns = [
    path("ajax/image/upload_profile/", views_ajax.ajax_upload_user_profile_image, name="ajax_upload_user_profile_image"),
    path("ajax/image/upload_cover/", views_ajax.ajax_upload_user_cover_image, name="ajax_upload_user_cover_image"),
    path("ajax/image/upload_gallery/", views_ajax.ajax_upload_user__gallery_image, name="ajax_upload_user__gallery_image"),
    path("ajax/image/<pk>/delete/", views_ajax.ajax_delete_user_image, name="ajax_delete_user_image"), 
]

urlpatterns += admin_urlpatterns
urlpatterns += htmx_urlpatterns
urlpatterns += ajax_urlpatterns


