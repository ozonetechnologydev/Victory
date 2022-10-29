from django.shortcuts import render, redirect,reverse
from django.http import HttpResponse, HttpResponseNotModified
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.forms import formset_factory
from django.http import HttpResponse

from datetime import datetime, timedelta

from main.decorators import allowed_users, admin_only
from academy.models import Branch, Department,  Subject, Section
from teachers.models import Teacher
from students.models import Student
from academy.forms import CreateBranchForm,CreateDepartmentForm, CreateSubjectForm,CreateSectionForm, UpdateBranchForm, UpdateDepartmentForm, UpdateSectionForm, UpdateSubjectForm
#===========================================================================




#===========================================================================
@admin_only
@login_required(login_url='login')
def academy_dashboard(request):

  branches = Branch.objects.all()
  branch_info = []
  for branch in branches:
    number_of_students = Student.objects.filter(sections__department__branch = branch).count()
    branch_info.append({"branch":branch, "number_of_students":number_of_students})


  departments = Department.objects.all()
  department_info = []
  for department in departments:
    number_of_students = Student.objects.filter(sections__department= department).count()
    department_info.append({"department":department, "number_of_students":number_of_students})


  subjects = Subject.objects.all()
  sections = Section.objects.all()

  branches_num = Branch.objects.count()
  departments_num = Department.objects.count()
  subjects_num = Subject.objects.count()
  sections_num = Section.objects.count()



  context = {
    "branch_info": branch_info,
    "department_info": department_info,
    "subjects": subjects,
    "sections" : sections,

    "branches_num": branches_num,
    "departments_num": departments_num,
    "subjects_num": subjects_num,
    "sections_num" : sections_num,
  }
    
  # print(Student.objects.aggregate())
  return render(request, "academy/admin/academy_dashboard.html", context)
#===========================================================================




  

#===========================================================================
@admin_only
@login_required(login_url='login')
def create_branch(request):
  form = CreateBranchForm()
  if request.method == "POST":
    form = CreateBranchForm(request.POST, request.FILES)
    if form.is_valid():
      branch = form.save()
      return redirect("branch_details", branch.id)
  context = {
    "form":form,
    "form_title":"Create Branch"
      }
  return render(request, "components/admin_form_page.html", context)
#===========================================================================





#===========================================================================
@admin_only
@login_required(login_url='login')
def branch_list(request):
  branches = Branch.objects.all()
  context = {"branches":branches}
  return render(request, "academy/admin/branch_list.html", context)
#===========================================================================





#===========================================================================
@login_required(login_url='login')
def branch_details(request, pk):

  branch = Branch.objects.get(id=pk)
  other_branches = Branch.objects.exclude(id=branch.id)

  branch_departments = Department.objects.filter(branch=branch)
  branch_subjects = Subject.objects.filter(department__branch=branch)
  branch_sections = Section.objects.filter(department__branch=branch)
  branch_teachers = Teacher.objects.filter(subject__department__branch=branch)
  branch_students = Student.objects.filter(sections__department__branch=branch)
  # review_form = BranchReviewForm()
  
  # if request.method == "POST":
  #   if request.POST.get("reviews") and request.POST.get("rating"):
  #     BranchReview.objects.create(
  #       reviewed=branch,
  #       reviewer=request.user,
  #       reviews=request.POST.get("reviews"),
  #       rating=int(request.POST.get("rating"))
  #     )
  
  context = {
    # "review_form":review_form,
    "branch":branch, 
    "other_branches":other_branches,
    "branch_departments":branch_departments,
    "branch_subjects":branch_subjects,
    "branch_sections":branch_sections, 
    "branch_teachers":branch_teachers,
    "branch_students":branch_students,
  }

  if request.user.is_superuser:
    return render(request, "academy/admin/branch_details.html", context)

  return render(request, "academy/branch_details.html", context)
#===========================================================================







#===========================================================================
@admin_only
@login_required(login_url='login')
def update_branch(request, pk):
  branch = Branch.objects.get(id=pk)
  form = UpdateBranchForm(instance=branch)

  if request.method == "POST":
    new_file = request.FILES.get("file")
    if not new_file in ["null", "Null", None, 'None', '']:
      context = {"success":False}
      try:
          branch.cover_image = new_file
          branch.save()
          context = {
              "success":True,
              "file_name":f"{new_file}",
              "file_view_url":branch.cover_image.url, 
          }
          print(context)
      except:
          return HttpResponseNotModified()
      return JsonResponse(context)
    
    form = UpdateBranchForm(request.POST,instance=branch)
    if form.is_valid():
      form.save()
      return redirect("branch_details", branch.id)


  context = {
    "form":form,
    "form_title":"Update Branch"
    }
  return render(request, "components/admin_form_page.html", context)
#===========================================================================






#===========================================================================
@admin_only
@login_required(login_url='login')
def delete_branch(request, pk):
  branch = Branch.objects.get(id=pk)
  branch.delete()
  return redirect("branch_list")
#===========================================================================





#===========================================================================
@admin_only
@login_required(login_url='login')
def create_department(request):
  form = CreateDepartmentForm()
  if request.method == "POST":
    form = CreateDepartmentForm(request.POST, request.FILES)
    if form.is_valid():
      department = form.save()
      return redirect("department_details", department.id)
  context = {
    "form":form,
    "form_title":"Create Department"
  }
  return render(request, "components/admin_form_page.html", context)
#===========================================================================






#===========================================================================
@admin_only
@login_required(login_url='login')
def department_list(request):
  departments = Department.objects.all()
  context = {"departments":departments}
  return render(request, "academy/admin/department_list.html", context)
#===========================================================================







#===========================================================================
@login_required(login_url='login')
def department_details(request, pk):

  department = Department.objects.get(id=pk)
  related_departments = Department.objects.filter(branch=department.branch).exclude(id=department.id)
  department_subjects = Subject.objects.filter(department=department)
  department_sections = Section.objects.filter(department=department)
  department_teachers = Teacher.objects.filter(subject__department=department)
  department_students = Student.objects.filter(sections__department=department)
  # review_form = DepartmentReviewForm()
  
  # if request.method == "POST":
  #   if request.POST.get("reviews") and request.POST.get("rating"):
  #     DepartmentReview.objects.create(
  #       reviewed=department,
  #       reviewer=request.user,
  #       reviews=request.POST.get("reviews"),
  #       rating=int(request.POST.get("rating"))
  #     )
  
  
  context = {
    # "review_form":review_form,
    "department":department, 
    "related_departments":related_departments,
    "department_subjects":department_subjects,
    "department_sections":department_sections, 
    "department_teachers":department_teachers,
    "department_students":department_students,
  }
  if request.user.is_superuser:
    return render(request, "academy/admin/department_details.html", context)
  return render(request, "academy/department_details.html", context)
#===========================================================================











#===========================================================================
@admin_only
@login_required(login_url='login')
def update_department(request, pk):
  dept = Department.objects.get(id=pk)
  form = UpdateDepartmentForm(instance=dept)

  if request.method == "POST":
    new_file = request.FILES.get("file")
    if not new_file in ["null", "Null", None, 'None', '']:
      context = {"success":False}
      try:
          dept.cover_image = new_file
          dept.save()
          context = {
              "success":True,
              "file_name":f"{new_file}",
              "file_view_url":dept.cover_image.url, 
          }
          print(context)
      except:
          return HttpResponseNotModified()
      return JsonResponse(context)
    
    form = UpdateDepartmentForm(request.POST, instance=dept)
    if form.is_valid():
      form.save()
      return redirect("department_details", dept.id)

  context = {"form":form, 
             "form_title":"Update Department"
             }
  return render(request, "components/admin_form_page.html", context)
#===========================================================================








#===========================================================================
@admin_only
@login_required(login_url='login')
def delete_department(request, pk):
  department = Department.objects.get(id=pk)
  department.delete()
  return redirect("department_list")
#===========================================================================






#===========================================================================
@admin_only
@login_required(login_url='login')
def create_subject(request):
  form = CreateSubjectForm()
  if request.method == "POST":
    form = CreateSubjectForm(request.POST)
    if form.is_valid():
      subject = form.save()
      return redirect("subject_details", subject.id)
  context = {
    "form":form,
    "form_title":"Create Subject"
  }
  return render(request, "components/admin_form_page.html", context)
#===========================================================================









#===========================================================================

@admin_only
@login_required(login_url='login')
def subject_list(request):
  subjects = Subject.objects.all()
  context = {"subjects":subjects}
  return render(request, "academy/admin/subject_list.html", context)
#===========================================================================








#===========================================================================
@login_required(login_url='login')
def subject_details(request, pk):

  subject = Subject.objects.get(id=pk)
  related_subjects = Subject.objects.filter(department=subject.department).exclude(id=subject.id)

  # subject_subjects = Subject.objects.filter(subject=subject)
  subject_sections = subject.section_set.all()
  subject_students = Student.objects.filter(sections__subjects=subject)
  
  teacher_subjects_num = Subject.objects.filter(teacher=subject.teacher).count()
  teacher_students_num = Student.objects.filter(sections__subjects__teacher=subject.teacher).count()
  
  # review_form = SubjectReviewForm()
  
  # if request.method == "POST":
  #   if request.POST.get("reviews") and request.POST.get("rating"):
  #     SubjectReview.objects.create(
  #       reviewed=subject,
  #       reviewer=request.user,
  #       reviews=request.POST.get("reviews"),
  #       rating=int(request.POST.get("rating"))
  #     )
  
  
  context = {
    # "review_form":review_form,
    "subject":subject, 
    "subject_sections":subject_sections, 
    "subject_students":subject_students,
    "teacher_subjects_num":teacher_subjects_num,
    "teacher_students_num":teacher_students_num,
    "related_subjects":related_subjects, 
  }
  if request.user.is_superuser:
    return render(request, "academy/admin/subject_details.html", context)

  return render(request, 'academy/course_details.html', context=context)
#===========================================================================









#===========================================================================
@admin_only
@login_required(login_url='login')
def update_subject(request, pk):
  subject = Subject.objects.get(id=pk)
  form = UpdateSubjectForm(instance=subject)

  if request.method == "POST":
    new_file = request.FILES.get("file")
    if not new_file in ["null", "Null", None, 'None', '']:
      context = {"success":False}
      try:
          subject.cover_image = new_file
          subject.save()
          context = {
              "success":True,
              "file_name":f"{new_file}",
              "file_view_url":subject.cover_image.url, 
          }
          print(context)
      except:
          return HttpResponseNotModified()
      return JsonResponse(context)
    
    
    form = UpdateSubjectForm(request.POST, instance=subject)
    if form.is_valid():
      form.save()
      return redirect("subject_details", subject.id)

  context = {
    "form":form, 
    "form_title":"Update Subject"
  }
  return render(request, "components/admin_form_page.html", context)
#===========================================================================








#===========================================================================
@admin_only
@login_required(login_url='login')
def delete_subject(request, pk):
  subject = Subject.objects.get(id=pk)
  subject.delete()
  return redirect("subjects_details")
#===========================================================================






#===========================================================================
@admin_only
@login_required(login_url='login')
def create_section(request):
  form = CreateSectionForm()
  if request.method == "POST":
    form = CreateSectionForm(request.POST, request.FILES)
    if form.is_valid():
      section = form.save()
    return redirect("section_details", section.id)
  context = {
    "form":form,
    "form_title":"Create Section"
  }
  return render(request, "components/admin_form_page.html", context)
#===========================================================================







#===========================================================================
@admin_only
@login_required(login_url='login')
def section_list(request):
  sections = Section.objects.all()
  context = {"sections":sections}
  return render(request, "academy/admin/section_list.html", context)
#===========================================================================







#=========================================================================
@login_required(login_url='login')
def section_details(request, pk):

  section = Section.objects.get(id=pk)
  related_sections = Section.objects.filter(department=section.department).exclude(id=section.id)

  section_subjects = section.subjects.all()
  section_teachers = Teacher.objects.filter(subject__section=section)
  section_students = Student.objects.filter(sections=section)

  # review_form = SubjectReviewForm()
  
  # if request.method == "POST":
  #   if request.POST.get("reviews") and request.POST.get("rating"):
  #     SectionReview.objects.create(
  #       reviewed=section,
  #       reviewer=request.user,
  #       reviews=request.POST.get("reviews"),
  #       rating=int(request.POST.get("rating"))
  #     )
  
  
  context = {
    # "review_form":review_form,
    "section":section, 
    "section_subjects":section_subjects,
    "section_teachers":section_teachers,
    "section_students":section_students,
    "related_sections":related_sections, 

  }
  if request.user.is_superuser:
    return render(request, "academy/admin/section_details.html", context)

  return render(request, "academy/section_details.html", context)
#===========================================================================








#===========================================================================
@admin_only
@login_required(login_url='login')
def update_section(request, pk):
  section = Section.objects.get(id=pk)
  form = UpdateSectionForm(instance = section)

  if request.method == "POST":
    new_file = request.FILES.get("file")
    if not new_file in ["null", "Null", None, 'None', '']:
      context = {"success":False}
      try:
          section.cover_image = new_file
          section.save()
          context = {
              "success":True,
              "file_name":f"{new_file}",
              "file_view_url":section.cover_image.url, 
          }
          print(context)
      except:
          return HttpResponseNotModified()
      return JsonResponse(context)
    
    form = UpdateSectionForm(request.POST, instance = section)
    if form.is_valid():
      form.save()
      print("success")
      return redirect("section_details", section.id)

  context = {
    "form":form,
    "form_title":"Update Section"
  }
  return render(request, "components/admin_form_page.html", context)
#===========================================================================








#===========================================================================
@admin_only
@login_required(login_url='login')
def delete_section(request, pk):
  section = Section.objects.get(id=pk)
  section.delete()
  return redirect("section_list")
#===========================================================================

