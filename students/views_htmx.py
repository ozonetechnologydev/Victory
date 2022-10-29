from django.shortcuts import render, reverse
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.hashers import make_password
#===========================================================================
from datetime import datetime, timedelta


#===========================================================================
from main.decorators import admin_only, allowed_users, unauthenticated
from accounts.forms import HtmxUserCreationForm, HtmxUserUpdateForm
from accounts.models import User
from students.models import Student
from students.forms import  AddStudentForm, HtmxAddStudentForm
from academy.models import Section
#===========================================================================


@login_required(login_url='/login')

@allowed_users(permissions = [
    "accounts.add_user",
    "accounts.change_user",
    "accounts.delete_user",
    
    "students.add_student",
    "students.change_student",
    "students.delete_student",
  
  ],require_all=True,  redirect_to='login')

def student_creation_tree(request):
  students = Student.objects.order_by("-admission_date")
  
  filter =  request.GET.get("filter")
  if filter in ["today", "last_week", "last_month", "last_year"]:
    today = datetime.today()
    last_date = today - timedelta(days=1)
    
    if filter == "last_week":
      last_date = today - timedelta(days=7)
    elif filter == "last_month":
      last_date = today - timedelta(days=30)
    elif filter == "last_year":
      last_date = today - timedelta(days=365)
  
    students = Student.objects.order_by("-admission_date").filter(admission_date__lte = today, admission_date__gt= last_date)
        
  student_form = AddStudentForm()
  context={
    "students":students,
    "title":"Add Student Information",
    "student_form":student_form,
  }
  if request.user.is_superuser:
    return render(request, "students/admin/students_creation_tree.html", context)
  
  
  return render(request, "students/register/students_creation_tree.html", context)




@login_required(login_url='login')
@allowed_users(permissions = [
    "accounts.add_user",
    "students.add_student",
  ],require_all=True,  redirect_to='login')
def htmx_user_and_student_create(request):
  user_form = HtmxUserCreationForm()
  student_form = HtmxAddStudentForm()
  
  if request.method == "POST":
    user_form = HtmxUserCreationForm(request.POST)
    student_form = HtmxAddStudentForm(request.POST)
    
    if user_form.is_valid():
      user = user_form.save()

      phone_number = request.POST.get('phone_number')
      sections = request.POST.getlist('sections')
      status = request.POST.getlist('status')
      simple_password = request.POST.get("password")
      password = make_password(simple_password)
      user.password= password
      user.save()
      student = Student.objects.create(
        user = user,
        phone_number = phone_number,
        status= status,
      )
    
        
      for section_id in sections:
        section = Section.objects.get(id = section_id)
        student.sections.add(section)
        
      student.save()
      messages.success(request, 'Student is created successfully.')
      print('Student is created successfully.')
      user_form = HtmxUserCreationForm()
      student_form = HtmxAddStudentForm()
  else:
    messages.info(request, 'You can create student new')
  
  form_list = [
     user_form, student_form, 
  ]
  
  context = {  
    "form_list":form_list,
    "title":"Create Account and Add Student Information",
    "action":reverse("htmx_user_and_student_create"),
  }
  return render(request, "components/multi_forms.html", context)


@login_required(login_url='login')
@allowed_users(permissions = [
    "accounts.change_user",
    "students.change_student",
  ],require_all=True,  redirect_to='login')
def htmx_user_and_student_update(request, pk):
  user = User.objects.get(id=pk)
  student = user.student
  
  user_form = HtmxUserUpdateForm(instance=user)
  student_form = HtmxAddStudentForm(instance=student)
  
  if request.method == "POST":
    user_form = HtmxUserUpdateForm(request.POST, instance=user)
    student_form = HtmxAddStudentForm(request.POST, instance=student)
    
    if user_form.is_valid() and student_form.is_valid():
      user = user_form.save()
      student = student_form.save()
      messages.success(request, 'Student is updated successfully.')
      print('Student is updated successfully.')

  else:
    messages.info(request, 'You can create student new')
  
  form_list = [
     user_form, student_form, 
  ]
  
  context = {  
    "form_list":form_list,
    "title":"Update Account and Student Information",
    "action":f"/students/htmx/user_and_student/{user.id}/update/",
  }
  return render(request, "components/multi_forms.html", context)

#===========================================================================

@login_required(login_url='login')
@allowed_users(permissions = [
    "students.add_student",
  ],require_all=True,  redirect_to='login')
def htmx_student_create(request):
  form = AddStudentForm()
  if request.method == "POST":
    form = AddStudentForm(request.POST, request.FILES)
    if form.is_valid():
      student = form.save()
      messages.success(request, 'Student is created successfully.')
      print('Student is created successfully.')
      form = AddStudentForm()
      
  else:
    messages.info(request, 'You can create student new')
  
  context = {  
    "form":form,
    "title":"Add Student Information",
    "action":reverse("htmx_student_create"),
  }
  return render(request, "components/forms.html", context)





@login_required(login_url='login')
@allowed_users(permissions = [
    "students.change_student",
  ],require_all=True,  redirect_to='login')
def htmx_student_update(request, pk):
  student = Student.objects.get(id=pk)
  form = AddStudentForm(instance=student)
  if request.method == "POST":
    form = AddStudentForm(request.POST, request.FILES, instance=student)
    if form.is_valid():
      student = form.save()
      messages.success(request, 'Student is =updated successfully.')
      print('Student is Updated successfully.')
  else:
    messages.info(request, 'You can update student new')
    
  context = {  
    "form":form,
    "title":"Update Student Information",
    "action":f"/academy/htmx/student/{student.id}/update/",
  }
  return render(request, "components/forms.html", context)



@login_required(login_url='login')
@allowed_users(permissions = [
    "students.delete_student",
  ],require_all=True,  redirect_to='login')
def htmx_student_delete(request, pk):
  student = Student.objects.get(id=pk)
  student.delete()
  return HttpResponse("")
#===========================================================================
