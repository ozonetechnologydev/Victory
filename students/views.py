from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.http import JsonResponse

from datetime import datetime, timedelta


from accounts.forms import AddressForm, PassChangeForm, RegisterForm, updateProfileForm, updateUserForm
from main.decorators import admin_only, allowed_users, unauthenticated
from students.models import Student
from students.forms import AddStudentForm, ApplyStudentForm1, ApplyStudentForm2, ApplyStudentForm3

# Create your views here.

#===========================================================================

@login_required(login_url='login')
def apply_student1(request):
  form = ApplyStudentForm1()
  if request.method == "POST":
     
    form = ApplyStudentForm1(request.POST)
    if form.is_valid():
      if not request.POST.get("branch") in [None,"none",'None','null',""]:
        request.session["branch_id"] = form.cleaned_data.get("branch").id
        
      student, created = Student.objects.get_or_create(user=request.user)
      return redirect("apply_student2")
        
        
  context = {
    "form":form,
    }
  return render(request, "students/public/apply_student.html", context)


def apply_student2(request):

  branch_id = request.session.get("branch_id")
  form = ApplyStudentForm2(branch_id=branch_id, instance=request.user.student)
    
  if request.method == "POST":
    form = ApplyStudentForm2(branch_id=branch_id, data=request.POST, instance=request.user.student)
    if not request.POST.get("department") in [None,"none",'None','null',""]:
      request.session["department_id"] = form.cleaned_data.get("department").id 
      
    if not request.POST.get("level") in [None,"none",'None','null',""]:
      request.session["level"] = form.cleaned_data.get("level")
      
    return redirect("apply_student3")
    
  context = {
    "form":form,
    "action":reverse("apply_student2")
  }
  return render(request, "components/forms.html", context)

  


def apply_student3(request):
  department_id = request.session.get("department_id")
  level = request.session.get("level")
  form = ApplyStudentForm3(department_id=department_id,level=level, instance=request.user.student)

  if request.method == "POST":
    form = ApplyStudentForm3(department_id=department_id,level=level, data=request.POST, instance=request.user.student)
    if form.is_valid():
      print(form)
      if not form.cleaned_data.get("sections") is None:
        form.save()
      del request.session["branch_id"]
      del request.session["department_id"]
      del  request.session["level"]
      context = {
        "form":form,
        "action":reverse("apply_student2")
      }
      return render(request, "students/components/welcome.html", context)
    
  context = {
    "form":form,
    "action":reverse("apply_student3")
  }
  return render(request, "components/forms.html", context)




#===========================================================================


#===========================================================================
@admin_only
@login_required(login_url='/login')
def create_student(request):
  form = AddStudentForm()

  if request.method == "POST":
    form = AddStudentForm(request.POST)
    if form.is_valid():
      print(request.POST)
      student = form.save()
      return redirect("user_details", student.user.id)

  context = {"form":form}
  return render(request, "components/admin_form_page.html", context)
#===========================================================================




#===========================================================================
@admin_only
@login_required(login_url='login')
def students_list(request):
  students_list = Student.objects.all().order_by("-user__date_joined")
  context = {"students":students_list,}
  return render(request, "students/admin/students_list.html", context)
#===========================================================================



#===========================================================================
@login_required(login_url='/login')
def update_students(request, pk):
  student = Student.objects.get(id=pk)
  form = AddStudentForm(instance=student)

  if request.method == "POST":
    form = AddStudentForm(request.POST, instance = student)
    
    if form.is_valid():
      form.save()
      return redirect("user_details", student.user.id)

  context = {"form":form,}
  return render(request, "components/admin_form_page.html", context)
#===========================================================================


#===========================================================================
@admin_only
@login_required(login_url='login')
def multi_update_students(request):
  students_id = request.POST.getlist("columns")
  print(students_id)
  students = Student.objects.filter(id__in=students_id)
  action = request.POST.get("action")
  if students.exists() and not action in ["null", None, "None", [], '[]', [''], '']:
    for student in students:
      if action == "delete":
        student.delete()
        print("student is deleted")
        
      elif action == "payed":
        student.payment = "payed"
        student.save()
        print("student is payed")
        
      elif action == "unpaid":
        student.payment = "unpaid"
        student.save()
        print("student is unpaid")
              
      elif action == "applied":
        student.status = "applied"
        student.save()
        print("student is applied")
              
      elif action == "pending":
        student.status = "pending"
        student.save()
        print("student is pending")
        
      elif action == "dismissed":
        student.status = "dismissed"
        student.save()
        print("student is dismissed")
      print(student.status)
        
  redirect_to = request.META.get("HTTP_REFERER")
  if not redirect_to in ["null", None, "None", [], '[]', [''], '']:
      redirect_to = "students_list"
  return redirect(redirect_to)

#===========================================================================




#===========================================================================
@admin_only
@login_required(login_url='/login')
def delete_students(request, pk):
  student = Student.objects.get(id=pk)
  student.delete()
  return redirect("students_list")
#===========================================================================

