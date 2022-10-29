from django.urls import path
from . import views, views_htmx, views_ajax

urlpatterns = [
#===========================================================================
    path("list/", views.blog_list, name="blog_list"),
    path("<pk>/details/", views.blog_details, name="blog_details"),
#===========================================================================
]
admin_urlpatterns = [

    path("admin/create/", views.admin_create_blog, name="admin_create_blog"),
    path("admin/overview/", views.admin_blog_overview, name="admin_blog_overview"),
    path("admin/list/", views.admin_blog_list, name="admin_blog_list"),
    path("admin/<pk>/details/", views.admin_update_blog, name="admin_details_blog"),
    path("admin/<pk>/update/", views.admin_update_blog, name="admin_update_blog"),
    path("admin/<pk>/duplicate/", views.admin_duplicate_blog, name="admin_duplicate_blog"),
    path("admin/<pk>/publish/", views.admin_publish_blog, name="admin_publish_blog"),
    path("admin/<pk>/unpublish/", views.admin_unpublish_blog, name="admin_unpublish_blog"),
    path("admin/<pk>/delete/", views.admin_delete_blog, name="admin_delete_blog"),
    
    
    path("admin/category/", views.admin_blog_category, name="admin_blog_category"),
    path("admin/category/create", views.admin_blog_create_category, name="admin_blog_create_category"),
    path("admin/category/<pk>/update/", views.admin_blog_update_category, name="admin_blog_update_category"),
    path("admin/category/<pk>/delete/", views.admin_blog_delete_category, name="admin_blog_delete_category"),
    
    
]

htmx_urlpatterns = [
    path("htmx/files/<image_pk>/delete_image/", views_htmx.htmx_delete_blog_image, name="htmx_delete_blog_image"), 
    path("htmx/files/<file_pk>/delete_file/", views_htmx.htmx_delete_blog_file, name="htmx_delete_blog_file"), 
    
    path("htmx/<pk>/comment/create/", views_htmx.htmx_create_blog_comment, name="htmx_create_blog_comment"), 
    path("htmx/<blog_pk>/comment/<comment_pk>/update/", views_htmx.htmx_update_blog_comment, name="htmx_update_blog_comment"), 
    
    path("htmx/subscribe/", views_htmx.htmx_create_blog_subscriber, name="htmx_create_blog_subscriber"), 
    
    
]

ajax_urlpatterns = [
    path("ajax/<blog_pk>/files/upload/", views_ajax.ajax_upload_blog_file, name="ajax_upload_blog_file"),
    path("ajax/files/<image_pk>/delete_image/", views_ajax.ajax_delete_blog_image, name="ajax_delete_blog_image"), 
    path("ajax/files/<file_pk>/delete_file/", views_ajax.ajax_delete_blog_file, name="ajax_delete_blog_file"), 
]

urlpatterns += admin_urlpatterns
urlpatterns += htmx_urlpatterns
urlpatterns += ajax_urlpatterns
