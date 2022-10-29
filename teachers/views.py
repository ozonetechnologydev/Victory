from django.shortcuts import render, redirect
from django.http import  JsonResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


from students.models import Student
from teachers.models import Teacher
from main.decorators import admin_only, allowed_users, unauthenticated
from accounts.forms import AddressForm, PassChangeForm, updateProfileForm, updateUserForm
from teachers.forms import AddTeacherForm

# Create your views here.
#===========================================================================
@login_required(login_url='login')
# @allowed_users(allowed_roles=['teachers'])
def teacher_profile(request):

  teacher_subjects =  []
  for subject in request.user.teacher.subject_set.all():
    teacher_subjects.append({"subject":subject,"students_num":Student.objects.filter(sections__subjects = subject).count()})
  
  teacher_students = Student.objects.filter(
    sections__subjects__teacher = request.user.teacher
  )
  print(teacher_students, teacher_subjects)
  password_form = PassChangeForm(user = request.user)
  account_form = updateUserForm(instance = request.user)
  address_form = AddressForm(instance = request.user.address)
  profile_form = updateProfileForm(instance = request.user)
  context = {
    "password_form":password_form,
    "account_form":account_form,
    "address_form":address_form,
    "profile_form":profile_form,
    "students_list":teacher_students,
    "teacher_subjects":teacher_subjects# request.user.teacher.subject_set.all()
  }

    
  return render(request, "users/public/user_profile.html", context)
#===========================================================================


#===========================================================================
@admin_only
@login_required(login_url='login')
def create_teacher(request):
  form = AddTeacherForm()

  if request.method == "POST":
    form = AddTeacherForm(request.POST)
    if form.is_valid():
      teacher = form.save()
      return redirect("user_details", teacher.user.id)

  context = {"form":form}
  return render(request, "teachers/admin/create_update_teacher.html", context)
#===========================================================================


#===========================================================================
@admin_only
@login_required(login_url='login')
def teachers_list(request):
  teachers_list = Teacher.objects.all().order_by("-user__date_joined")
  context = {"teachers":teachers_list}
  return render(request, "teachers/admin/teachers_list.html", context)
#===========================================================================





#===========================================================================
@admin_only
@login_required(login_url='login')
def update_teachers(request, pk):
  teacher = Teacher.objects.get(id=pk)

  form = AddTeacherForm(instance=teacher)

  if request.method == "POST":
    form = AddTeacherForm(request.POST, instance = teacher)
    
    if form.is_valid():
      form.save()
      redirect_to = request.META.get("HTTP_REFERER")
      return redirect("user_details", teacher.user.id)

  context = {
    "form":form,
    "form_title":"Update Teachers Info"
  }
  return render(request, "components/admin_form_page.html", context)
#===========================================================================


#===========================================================================
@admin_only
@login_required(login_url='login')
def delete_teachers(request, pk):
  teacher = Teacher.objects.get(id=pk)
  teacher.delete()
  return redirect("teachers_list")
#===========================================================================



#===========================================================================
@admin_only
@login_required(login_url='login')
def htmx_delete_teachers(request, pk):
  teacher = Teacher.objects.get(id=pk)
  teacher.delete()
  return HttpResponse("")
#===========================================================================