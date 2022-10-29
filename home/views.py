from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from accounts.models import User
from home.models import Contact
from home.forms import CreateContactForm
from main.forms import ApplyStudentForm
from academy.models import Branch, Department,Section, Subject
from main.models import AboutUs, CoreValue, Gallery, Team
from teachers.models import  Teacher
from students.models import  Student


# Create your views here.
def home(request):
  users = User.objects.all()
  students = Student.objects.all()
  teachers = Teacher.objects.all()

  branches = Branch.objects.all()
  departments = Department.objects.all()
  subjects = Subject.objects.all()[:10]
  sections = Section.objects.all()
  
  context = {
    "users":users,
    "students":students,
    "teachers":teachers,
    
    "branches":branches,
    "departments":departments,
    "subjects":subjects,
    "sections":sections,
  }
  return render(request, "home/public/home.html", context)



#===========================================================================
 







#===========================================================================

def academy_home(request):
  users = User.objects.all()
  students = Student.objects.all()
  teachers = Teacher.objects.all()

  branches = Branch.objects.all()
  departments = Department.objects.all()
  subjects = Subject.objects.all()
  sections = Section.objects.all()
  
  context = {
    "users":users,
    "students":students,
    "teachers":teachers,
    
    "branches":branches,
    "departments":departments,
    "subjects":subjects,
    "sections":sections,
  }

  return render(request, "academy/public/academy_home.html", context)

#===========================================================================


def course_filter_list(request):
  branches = Branch.objects.all()
  departments = Department.objects.all()
  subjects = Subject.objects.all()
  context = {
    "branches":branches,
    "departments":departments,
    "subjects":subjects,
    }
  return render(request, "academy/public/course_filter_list.html", context)

 
#===========================================================================

def about(request):
  about_us = AboutUs.objects.all()
  core_values = CoreValue.objects.all()
  teams = Team.objects.all()
  num_branches = Branch.objects.count()
  num_students = Student.objects.count()
  num_teachers = Teacher.objects.count()
  num_subjects = Subject.objects.count()
  context = {
    "about_us":about_us,
    "core_values":core_values,
    "teams":teams,
    "num_branches":num_branches,
    "num_students":num_students,
    "num_teachers":num_teachers,
    "num_subjects":num_subjects,
  
  }
  return render(request, "home/public/about.html", context)

def contact(request):
  form = CreateContactForm()
  if request.method == "POST":
    form = CreateContactForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect("home")
  context = {"form":form}
  return render(request, "home/public/contact.html", context)

def contact_list(request):
  contacts = Contact.objects.all()
  context = {"contacts":contacts}
  return render(request, "home/admin/contact_list.html", context)

def gallery(request):
  galleries = Gallery.objects.all()
  context = {"galleries":galleries}
  return render(request, "home/public/gallery.html", context)

