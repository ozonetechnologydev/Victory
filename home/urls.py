from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("academy_home/", views.academy_home, name="academy_home"),
    path("course_filter_list/", views.course_filter_list, name="course_filter_list"),
    

    path("contact/", views.contact, name="contact"),
    path("contact_list/", views.contact_list, name="contact_list"),
    path("about/", views.about, name="about"),
    path("gallery/", views.gallery, name="gallery"),

    
]
