from django.contrib.auth import views as auth_views
from django.urls import path
from quiz import views, views_htmx
urlpatterns = [
    path("", views.quiz, name="quiz"),
    path("list/", views.quizzes_list, name="quizzes_list"),
    path("<pk>/take/", views.take_quizzes, name="take_quizzes"),
    
]


htmx_urlpatterns = [
    path("htmx/creation_tree/", views_htmx.quiz_creation_tree, name="quiz_creation_tree"),
    
    
#===========================================================================
    path("htmx/create/", views_htmx.htmx_quiz_create, name="htmx_quiz_create"),
    path("htmx/<pk>/update/", views_htmx.htmx_quiz_update, name="htmx_quiz_update"),
    path("htmx/<pk>/delete/", views_htmx.htmx_quiz_delete, name="htmx_quiz_delete"),
#===========================================================================
    
    
#===========================================================================
    path("htmx/<pk>/question/create/", views_htmx.htmx_question_create, name="htmx_question_create"),
    path("htmx/question/<pk>/update/", views_htmx.htmx_question_update, name="htmx_question_update"),
    path("htmx/question/<pk>/delete/", views_htmx.htmx_question_delete, name="htmx_question_delete"),
#===========================================================================
    
    
#===========================================================================
    path("htmx/question/<pk>/answer/create/", views_htmx.htmx_answer_create, name="htmx_answer_create"),
    path("htmx/answer/<pk>/update/", views_htmx.htmx_answer_update, name="htmx_answer_update"),
    path("htmx/answer/<pk>/delete/", views_htmx.htmx_answer_delete, name="htmx_answer_delete"),
#===========================================================================
     
]
urlpatterns += htmx_urlpatterns