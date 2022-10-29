#===========================================================================
from django.shortcuts import render, redirect,reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import permission_required
from academy.models import Subject

from accounts.models import User
from teachers.models import Teacher
from students.models import Student
from main.decorators import admin_only, allowed_users, unauthenticated
from django.db.models import Q
from accounts.forms import AddressForm, AdminPassChangeForm, PassChangeForm, UserChangeForm, updateProfileForm, updateUserForm

from users.forms import UserGroupForm
#===========================================================================

#===========================================================================


#===========================================================================
@login_required(login_url='login')
def user_profile(request):
  user = User.objects.get(id= request.user.id)
  account_form = updateUserForm(instance = user)
  address_form = AddressForm(instance = user.address)
  profile_form = updateProfileForm(instance = user)

  password_form = PassChangeForm(user = user)
  
  if user.is_superuser:
    password_form = AdminPassChangeForm(user = user)
    
  context = {
    "password_form":password_form,
    "account_form":account_form,
    "address_form":address_form,
    "profile_form":profile_form,
  }
  teachers = Teacher.objects.filter(user=user)
  students = Student.objects.filter(user=user)
  if teachers.exists():
    teacher_subjects =  []
    for subject in teachers.first().subject_set.all():
      teacher_subjects.append({"subject":subject,"students_num":Student.objects.filter(sections__subjects = subject).count()})
    
    teacher_students = Student.objects.filter(
      sections__subjects__teacher = teachers
    )
    context["students_list"] = teacher_students
    context["teacher_subjects"] = teacher_subjects
    
  if students.exists() and not user.is_superuser and not teachers.exists():
    context["student_subjects"] = Subject.objects.filter(section__student=students.first())
 
  
  return render(request, "users/public/user_profile.html",context)
#===========================================================================


#===========================================================================
@login_required(login_url='login')
def update_user_profile(request):
  form = updateProfileForm(instance = request.user)
  context = {
        "show_messages":True,
        "title":"Edit Profile",
        "action":reverse("update_user_profile"),
    }
  if request.method in ('PUT', 'POST'):
    form = updateProfileForm(request.POST, request.FILES, instance=request.user)
    if form.is_valid():
        form.save()
        messages.success(request, 'Profile is Updated successfully.')
        context = {
            **context,
            "form":form,
            "alert":{"title":"success","body":"profile is updated successfully","type":"success",},
        }

  return render(request, "components/forms.html", context)
#===========================================================================

#===========================================================================
@login_required(login_url='login')
def update_user_address(request):
    form = AddressForm(instance = request.user.address)
    
    context = {
        "form":form,
        "show_messages":True,
        "title":"Edit Address",
        "action":reverse("update_user_address"),
    } 
    
    if request.method in ('PUT', 'POST'):
        form = AddressForm(request.POST, instance=request.user.address)
        if form.is_valid():
            form.save()
            messages.success(request, 'Address is Update successfully.')
            context = {
                **context,
                "form":form,
                "alert":{"title":"Success","body":"Address is updated successfully","type":"success",},
            }
            
    return render(request, "components/forms.html", context)
#===========================================================================
#===========================================================================





#===========================================================================
@admin_only
@login_required(login_url='login')
def users_list(request):
  
  print(request.POST)
  
  users_list = User.objects.all().order_by("-date_joined")
  groups = Group.objects.all()
  context = {
    'users_list': users_list,
    'groups': groups,
    }
  return render(request, "users/admin/users_list.html", context)
#===========================================================================


#===========================================================================
@login_required(login_url='login')
def user_details(request, pk):
  user = User.objects.get(id=pk)
  if user == request.user:
    return redirect("user_profile")

  teacher=Teacher.objects.filter(user=user)
  student=Student.objects.filter(user=user)

  if teacher.exists():
    context = {"teacher":teacher.first()}
    return render(request, "teachers/admin/teacher_profile.html", context)
  elif student.exists():
    context = {"student":student.first()}
    return render(request, "students/admin/student_profile.html", context)

  context = {"user":user}
  return render(request, "users/admin/user_profile.html", context)
#===========================================================================


#===========================================================================
@admin_only
@login_required(login_url='login')
def change_user(request, pk):
    user = User.objects.get(id=pk)
    form = UserChangeForm(instance=user)

    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance = user)
        
        if form.is_valid():
          form.save()
          return redirect("user_details", user.id)

    context = {'form':form, }
    return render(request, 'users/admin/change_user.html', context)
#===========================================================================



#===========================================================================


#===========================================================================
@admin_only
@login_required(login_url='login')
def create_user_group(request):
    form = UserGroupForm()
    if request.method == 'POST':
        form = UserGroupForm(request.POST)
        if form.is_valid():
            group = form.save()
            return redirect("users_list")

    context = {'form': form,}
    return render(request, 'users/admin/create_user_group.html', context)
#===========================================================================


#===========================================================================
@admin_only
@login_required(login_url='login')
def update_user_group(request, pk):

    group = Group.objects.get(id = pk)
    form = UserGroupForm(instance=group)
    if request.method == 'POST':
        form = UserGroupForm(request.POST, instance=group)
        if form.is_valid():
            group = form.save()
            return redirect("users_list")

    context = {'form': form,}
    return render(request, 'users/admin/create_user_group.html', context)
#===========================================================================


