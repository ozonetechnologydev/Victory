from django.shortcuts import render, reverse
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#===========================================================================
from datetime import datetime, timedelta


#===========================================================================
from academy.models import Branch, Department,  Subject, Section
from academy.forms import  CreateBranchForm, CreateSubjectForm, HtmxCreateBranchForm,HtmxCreateDepartmentForm, HtmxCreateSubjectForm,HtmxCreateSectionForm
from main.decorators import allowed_users
#===========================================================================





@login_required(login_url='login')

@allowed_users(permissions = [
    "academy.add_branch",
    "academy.change_branch",
    "academy.delete_branch",
    
    "academy.add_department",
    "academy.change_department",
    "academy.delete_department",
    
    "academy.add_subject",
    "academy.change_subject",
    "academy.delete_subject",
    
    "academy.add_section",
    "academy.change_section",
    "academy.delete_section",
  ], require_all=True, redirect_to='login')

def academy_creation_tree(request):
  branches = Branch.objects.order_by("-created")
  if request.GET.get("filter") and request.GET.get("filter") != "all":
        today = datetime.today()
        last_date = today - timedelta(days=1)
        
        filter =  request.GET.get("filter")
        
        if filter == "last_week":
          last_date = today - timedelta(days=7)
        if filter == "last_month":
          last_date = today - timedelta(days=30)
        if filter == "last_year":
          last_date = today - timedelta(days=365)

        branches = Branch.objects.order_by("-created").filter(created__lte = today, created__gt= last_date)
        
        
  branch_form = CreateBranchForm()

  context={
    "branches":branches,
    "form_title":"Create Branch",
    "branch_form":branch_form,
  }
  
  if request.user.is_superuser:
    return render(request, "academy/admin/academy_create_tree.html", context)
    
  return render(request, "academy/register/academy_creation_tree.html", context)



#===========================================================================

@login_required(login_url='login')
@allowed_users(permissions = ["academy.add_branch"], redirect_to='login')
def htmx_branch_create(request):
  form = HtmxCreateBranchForm()
  if request.method == "POST":
    form = HtmxCreateBranchForm(request.POST)
    if form.is_valid():
      branch = form.save()
      messages.success(request, 'Branch is created successfully.')
      print('Branch is created successfully.')
      form = HtmxCreateBranchForm()
  else:
    messages.info(request, 'You can create branch new')
  
  context = {  
    "form":form,
    "form_title":"Create Branch",
    "show_messages":True,
    "action":f"/academy/htmx/branch/create/",
  }
  return render(request, "components/forms.html", context)


@login_required(login_url='login')
@allowed_users(permissions = ["academy.change_branch",], redirect_to='login')
def htmx_branch_update(request, pk):
  branch = Branch.objects.get(id=pk)
  form = HtmxCreateBranchForm(instance=branch)
  if request.method == "POST":
    form = HtmxCreateBranchForm(request.POST, instance=branch)
    if form.is_valid():
      branch = form.save()
      messages.success(request, 'Branch is =updated successfully.')
      print('Branch is Updated successfully.')
      
      
  else:
    messages.info(request, 'You can update branch new')
    
  context = {  
    "form":form,
    "form_title":"Update Branch",
    "show_messages":True,
    "action":f"/academy/htmx/branch/{branch.id}/update/",
  }
  return render(request, "components/forms.html", context)


@login_required(login_url='login')
@allowed_users(permissions = ["academy.delete_branch",], redirect_to='login')
def htmx_branch_delete(request, pk):
  branch = Branch.objects.get(id=pk)
  branch.delete()
  return HttpResponse("")
#===========================================================================


#===========================================================================

@login_required(login_url='login')
@allowed_users(permissions = ["academy.add_department"], redirect_to='login')
def htmx_branch_department_create(request, pk):
  print(request.POST)
  branch = Branch.objects.get(id=pk)
  form = HtmxCreateDepartmentForm()
  if request.method == "POST":
    form = HtmxCreateDepartmentForm(request.POST)
    if form.is_valid():
      department = form.save()
      department.branch = branch
      department.save()
      messages.success(request, 'Department is created successfully.')
      print('Department is created successfully.')
      form = HtmxCreateDepartmentForm()
  else:
    messages.info(request, 'You can create department new')
    
  print(branch.department_set.all())
  context = {  
    "form":form,
    "form_title":"Create Department",
    "show_messages":True,
    "action":f"/academy/htmx/branch/{branch.id}/department/create/",
  }
  return render(request, "components/forms.html", context)


@login_required(login_url='login')
@allowed_users(permissions = ["academy.change_department"], redirect_to='login')
def htmx_department_update(request, pk):
  print(request.POST)
  department = Department.objects.get(id=pk)
  form = HtmxCreateDepartmentForm(instance=department)
  if request.method == "POST":
    form = HtmxCreateDepartmentForm(request.POST, instance=department)
    if form.is_valid():
      department = form.save()
      messages.success(request, 'Department is updated successfully.')
      print('Department is Updated successfully.')
  else:
    messages.info(request, 'You can update department new')
    
  context = {  
    "form":form,
    "form_title":"Update Department",
    "show_messages":True,
    "action":f"/academy/htmx/department/{department.id}/update/",
  }
  return render(request, "components/forms.html", context)

@login_required(login_url='login')
@allowed_users(permissions = ["academy.delete_department"], redirect_to='login')
def htmx_department_delete(request, pk):
  department = Department.objects.get(id=pk)
  department.delete()
  return HttpResponse("")
#===========================================================================



#===========================================================================
@login_required(login_url='login')
@allowed_users(permissions = ["academy.add_subject"], redirect_to='login')
def htmx_branch_subject_create(request, pk):
  branch = Branch.objects.get(id=pk)
  form = HtmxCreateSubjectForm(branch_id = branch.id)
  if request.method == "POST":
    form = HtmxCreateSubjectForm(branch_id = branch.id, data=request.POST)
    if form.is_valid():
      subject = form.save()
        
      department_id = request.POST.get("department")
      print(department_id)
      if not department_id in [None, 'None',  '', 'none', 'null']:
        subject.department = branch.department_set.get(id=department_id)
        subject.save()
        
        
      messages.success(request, 'Subject is created successfully.')
      
      form = HtmxCreateSubjectForm(branch_id = branch.id)
  else:
    messages.info(request, 'You can create subject new')
    

  context = {  
    "form":form,
    "form_title":"Create Subject",
    "show_messages":True,
    "action":f"/academy/htmx/branch/{branch.id}/subject/create/",
  }
  return render(request, "components/forms.html", context)


#===========================================================================
@login_required(login_url='login')
@allowed_users(permissions = ["academy.add_subject"], redirect_to='login')
def htmx_department_subject_create(request, pk):
  department = Department.objects.get(id=pk)
  form = HtmxCreateSubjectForm()
  if request.method == "POST":
    form = HtmxCreateSubjectForm(data=request.POST)
    form.clean_name_and_department(request.POST.get("name"), department)
    if form.is_valid():
        subject = form.save()
        subject.department = department
        subject.save()
        messages.success(request, 'Subject is created successfully.')
        
        form = HtmxCreateSubjectForm()
  else:
    messages.info(request, 'You can create subject new')
    
  context = {  
    "form":form,
    "form_title":"Create Subject",
    "show_messages":True,
    "action":f"/academy/htmx/department/{department.id}/subject/create/",
  }
  return render(request, "components/forms.html", context)


#===========================================================================
@login_required(login_url='login')
@allowed_users(permissions = ["academy.add_subject"], redirect_to='login')
def htmx_section_subject_create(request, pk):
  section = Section.objects.get(id=pk)
  department = Department.objects.get(id=section.department.id)
  
  form = HtmxCreateSubjectForm()
  if request.method == "POST":
    form = HtmxCreateSubjectForm(data=request.POST)
    form.clean_name_and_department(request.POST.get("name"), department)
    if form.is_valid():
        subject = form.save()
        subject.department = department
        subject.save()
        
        section.subjects.add(subject)
        section.save()
        
        messages.success(request, 'Subject is created successfully.')
        
        form = HtmxCreateSubjectForm()
  else:
    messages.info(request, 'You can create subject new')
    
  context = {  
    "form":form,
    "form_title":"Create Subject",
    "show_messages":True,
    "action":f"/academy/htmx/section/{section.id}/subject/create/",
  }
  return render(request, "components/forms.html", context)

@login_required(login_url='login')
@allowed_users(permissions = ["academy.change_subject"], redirect_to='login')
def htmx_subject_update(request, pk):
  subject = Subject.objects.get(id=pk)
  form = HtmxCreateSubjectForm(instance=subject)
  if request.method == "POST":
    form = HtmxCreateSubjectForm(request.POST, instance=subject)
    if form.is_valid():
      subject = form.save()
      messages.success(request, 'Subject is updated successfully.')
      print('subject is Updated successfully.')
  else:
    messages.info(request, 'You can update subject new')
    
  context = {  
    "form":form,
    "form_title":"Update Subject",
    "show_messages":True,
    "action":f"/academy/htmx/subject/{subject.id}/update/",
  }
  return render(request, "components/forms.html", context)


@login_required(login_url='login')
@allowed_users(permissions = ["academy.delete_subject"], redirect_to='login')
def htmx_subject_delete(request, pk):
  subject = Subject.objects.get(id=pk)
  subject.delete()
  return HttpResponse("")
#===========================================================================



#===========================================================================


@login_required(login_url='login')
@allowed_users(permissions = ["academy.add_section"], redirect_to='login')
def htmx_branch_section_create(request, pk):
  print(request.POST)
  branch = Branch.objects.get(id=pk)
  form = HtmxCreateSectionForm(branch_id = branch.id)
  print(dir(form))
  if request.method == "POST":
    form = HtmxCreateSectionForm(branch_id = branch.id, data=request.POST)
    if form.is_valid():
      section = form.save()
      
      department_id = request.POST.get("department")
      print(department_id)
      if not department_id in [None, 'None',  '', 'none', 'null']:
        section.department = branch.department_set.get(id=department_id)
        section.save()
      
      messages.success(request, 'Section is created successfully.')
      print('section is created successfully.')
      form = HtmxCreateSectionForm(branch_id = branch.id)
  else:
    messages.info(request, 'You can create section new')

  context = {  
    "form":form,
    "form_title":"Create Section",
    "show_messages":True,
    "action":f"/academy/htmx/branch/{branch.id}/section/create/",
  }
  return render(request, "components/forms.html", context)

#===========================================================================


@login_required(login_url='login')
@allowed_users(permissions = ["academy.add_section"], redirect_to='login')
def htmx_department_section_create(request, pk):
  print(request.POST)
  department = Department.objects.get(id=pk)
  form = HtmxCreateSectionForm(department_id=department.id)
  if request.method == "POST":
    form = HtmxCreateSectionForm(data=request.POST)
    form.clean_name_and_department(request.POST.get("name"),request.POST.get("shift_time"), department)
    if form.is_valid():
      section = form.save()
      section.department = department
      section.save()
      messages.success(request, 'Section is created successfully.')
      print('section is created successfully.')
      form = HtmxCreateSectionForm(department_id=department.id)
  else:
    messages.info(request, 'You can create section new')
    
  print(department.section_set.all())
  context = {  
    "form":form,
    "form_title":"Create Section",
    "show_messages":True,
    "action":f"/academy/htmx/department/{department.id}/section/create/",
  }
  return render(request, "components/forms.html", context)


@login_required(login_url='login')
@allowed_users(permissions = ["academy.change_section"], redirect_to='login')
def htmx_section_update(request, pk):
  section = Section.objects.get(id=pk)
  form = HtmxCreateSectionForm(section.department.id, instance=section)
  if request.method == "POST":
    form = HtmxCreateSectionForm(request.POST, instance=section)
    if form.is_valid():
      section = form.save()
      messages.success(request, 'Section is updated successfully.')
      print('section is Updated successfully.')
  else:
    messages.info(request, 'You can update section new')
    
  context = {  
    "form":form,
    "form_title":"Update Section",
    "show_messages":True,
    "action":f"/academy/htmx/section/{section.id}/update/",
  }
  return render(request, "components/forms.html", context)



@login_required(login_url='login')
@allowed_users(permissions = ["academy.delete_section"], redirect_to='login')
def htmx_section_delete(request, pk):
  section = Section.objects.get(id=pk)
  section.delete()
  return HttpResponse("")
#===========================================================================
