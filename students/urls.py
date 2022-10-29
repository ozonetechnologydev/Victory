from django.contrib.auth import views as auth_views
from django.urls import path
from students import views, views_htmx
urlpatterns = [
    
    
    
    path("apply_student/", views.apply_student1, name="apply_student1"),
    path("apply_student/step2/", views.apply_student2, name="apply_student2"),
    path("apply_student/step3/", views.apply_student3, name="apply_student3"),
    
#===========================================================================
    path("admin/create/", views.create_student, name="create_student"),
    path("admin/list/", views.students_list, name="students_list"),
    path("admin/update/", views.multi_update_students, name="multi_update_students"),
    path("admin/<pk>/update/", views.update_students, name="update_students"),
    path("admin/<pk>/delete/", views.delete_students, name="delete_students"),
#===========================================================================


]


htmx_urlpatterns = [
    
#===========================================================================
    path("htmx/creation_tree/", views_htmx.student_creation_tree, name="student_creation_tree"),
    path("htmx/user_and_student/create/", views_htmx.htmx_user_and_student_create, name="htmx_user_and_student_create"),
    path("htmx/user_and_student/<pk>/update/", views_htmx.htmx_user_and_student_update, name="htmx_user_and_student_update"),
    
    
    path("htmx/student/create/", views_htmx.htmx_student_create, name="htmx_student_create"),
    path("htmx/student/<pk>/update/", views_htmx.htmx_student_update, name="htmx_student_update"),
    path("htmx/student/<pk>/delete/", views_htmx.htmx_student_delete, name="htmx_student_delete"),
#===========================================================================
  
]
urlpatterns += htmx_urlpatterns