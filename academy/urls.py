from django.urls import path
from . import views, views_htmx
urlpatterns = [


]

admin_urlpatterns = [

#===========================================================================
    path("admin/dashboard/", views.academy_dashboard, name="academy_dashboard"),
#===========================================================================
    
    
        
#===========================================================================
    path("admin/branch/create/", views.create_branch, name="create_branch"),
    path("admin/branch/list/", views.branch_list, name="branch_list"),
    path("admin/branch/<pk>/details/", views.branch_details, name="branch_details"),
    path("admin/branch/<pk>/update/", views.update_branch, name="update_branch"),
    path("admin/branch/<pk>/delete/", views.delete_branch, name="delete_branch"),
#===========================================================================

#===========================================================================
    path("admin/department/create/", views.create_department, name="create_department"),
    path("admin/department/list/", views.department_list, name="department_list"),
    path("admin/department/<pk>/details/", views.department_details, name="department_details"),
    path("admin/department/<pk>/update/", views.update_department, name="update_department"),
    path("admin/department/<pk>/delete/", views.delete_department, name="delete_department"),
#===========================================================================
    
#===========================================================================
    path("admin/subject/create/", views.create_subject, name="create_subject"),
    path("admin/subject/list/", views.subject_list, name="subject_list"),
    path("admin/subject/<pk>/update/", views.update_subject, name="update_subject"),
    path("admin/subject/<pk>/details/", views.subject_details, name="subject_details"),
    path("admin/subject/<pk>/delete/", views.delete_subject, name="delete_subject"),
#===========================================================================

#===========================================================================
    path("admin/section/create/", views.create_section, name="create_section"),
    path("admin/section/list/", views.section_list, name="section_list"),
    path("admin/section/<pk>/update/", views.update_section, name="update_section"),
    path("admin/section/<pk>/details/", views.section_details, name="section_details"),
    path("admin/section/<pk>/delete/", views.delete_section, name="delete_section"),
#===========================================================================

]

htmx_urlpatterns = [
    path("htmx/creation_tree/", views_htmx.academy_creation_tree, name="academy_creation_tree"),
    
#===========================================================================
    path("htmx/branch/create/", views_htmx.htmx_branch_create, name="htmx_branch_create"),
    path("htmx/branch/<pk>/update/", views_htmx.htmx_branch_update, name="htmx_branch_update"),
    path("htmx/branch/<pk>/delete/", views_htmx.htmx_branch_delete, name="htmx_branch_delete"),
#===========================================================================
    
    
#===========================================================================
    path("htmx/branch/<pk>/department/create/", views_htmx.htmx_branch_department_create, name="htmx_branch_department_create"),
    path("htmx/department/<pk>/update/", views_htmx.htmx_department_update, name="htmx_department_update"),
    path("htmx/department/<pk>/delete/", views_htmx.htmx_department_delete, name="htmx_department_delete"),
#===========================================================================
    
    
#===========================================================================
    path("htmx/branch/<pk>/subject/create/", views_htmx.htmx_branch_subject_create, name="htmx_branch_subject_create"),
    path("htmx/department/<pk>/subject/create/", views_htmx.htmx_department_subject_create, name="htmx_department_subject_create"),
    path("htmx/subject/<pk>/update/", views_htmx.htmx_subject_update, name="htmx_subject_update"),
    path("htmx/subject/<pk>/delete/", views_htmx.htmx_subject_delete, name="htmx_subject_delete"),
#===========================================================================
    
    
#===========================================================================
    path("htmx/branch/<pk>/section/create/", views_htmx.htmx_branch_section_create, name="htmx_branch_section_creation"),
    path("htmx/department/<pk>/section/create/", views_htmx.htmx_department_section_create, name="htmx_department_section_creation"),
    path("htmx/section/<pk>/subject/create/", views_htmx.htmx_section_subject_create, name="htmx_section_subject_create"),
    path("htmx/section/<pk>/update/", views_htmx.htmx_section_update, name="htmx_section_update"),
    path("htmx/section/<pk>/delete/", views_htmx.htmx_section_delete, name="htmx_section_delete"),
#===========================================================================
     
]
urlpatterns += admin_urlpatterns
urlpatterns += htmx_urlpatterns