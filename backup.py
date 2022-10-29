

#===========================================================================
@admin_only
@login_required(login_url='login')
def search_for_students(request):
    if request.method == "GET" and request.GET.get("search"):
      searching_for = request.GET.get("search")
     
      students = Student.objects.filter(
        Q(section__section_name__istartswith=searching_for)|
        Q(profile__user__first_name__istartswith=searching_for)|
        Q(profile__user__last_name__istartswith=searching_for)|
        Q(profile__user__username__istartswith=searching_for)|
        Q(profile__user__email__istartswith=searching_for) |
        Q(department__dept_name__istartswith=searching_for)
        )

      profile = Profile.objects.get(user=request.user)

      paginator = Paginator(students, 2) # Show 25 contacts per page.
      page_number = request.GET.get('page')
      page_obj = paginator.get_page(page_number)

      context = {
      "page_obj":page_obj, 
      "search":searching_for,
      "profile":profile,
      }
      print(students)
      return render(request, "dashboard/searching_result.html", context)
    context = {}
    return render(request, "dashboard/searching_result.html", context)
#===========================================================================



#===========================================================================
@admin_only
@login_required(login_url='login')
def search_for_users(request):
    if request.method == "GET" and request.GET.get("search"):
      searching_for = request.GET.get("search")

      profiles = Profile.objects.filter(
        Q(user__first_name__istartswith=searching_for)|
        Q(user__last_name__istartswith=searching_for)|
        Q(user__username__istartswith=searching_for)|
        Q(user__email__istartswith=searching_for)
        )
 
      profile = Profile.objects.get(user=request.user)

      paginator = Paginator(profiles, 2) # Show 25 contacts per page.
      page_number = request.GET.get('page')
      page_obj = paginator.get_page(page_number)

      context = {
      "page_obj":page_obj,

      "search":searching_for,
      "profile":profile,
      }
      print(students)
      return render(request, "dashboard/searching_result.html", context)
    context = {}
    return render(request, "dashboard/searching_result.html", context)
#===========================================================================




  if request.method == "POST":

    if request.POST.get("new_departments"):
      departments_id_list = request.POST.getlist("new_departments")
      
      for department_id in departments_id_list:
        department = Department.objects.get(id=department_id)
        department.branch = branch
        department.save()

    if request.POST.get("new_classes"):
      classes_id_list = request.POST.getlist("new_classes")

      for classe_id in classes_id_list:
        department = Department.objects.get(id=department_id)
        department.branch = branch
        classe = classe.objects.get(id=classe_id)
        classe.branch = branch
        classe.save()


    if request.POST.get("new_subjects"):
      subjects_id_list = request.POST.getlist("new_subjects")

      for subject_id in subjects_id_list:
        subject = Subject.objects.get(id=subject_id)
        department = subject.department
        department.branch = branch
        department.save()
        subject.save()


    if request.POST.get("new_students"):
      students_id_list = request.POST.getlist("students")
      print(students_id_list)
      for student_id in students_id_list:
        student = Student.objects.get(id=student_id)
        student.branch = branch
        student.save()

    if request.POST.get("new_students"):
      students_id_list = request.POST.getlist("students")
      print(students_id_list)
      for student_id in students_id_list:
        student = Student.objects.get(id=student_id)
        student.branch = branch
        student.save()

    if request.POST.get("new_students"):
      students_id_list = request.POST.getlist("students")
      print(students_id_list)
      for student_id in students_id_list:
        student = Student.objects.get(id=student_id)
        student.branch = branch
        student.save()


  context={}
  if request.GET.get("list") == "other_departments":
    other_departments = Department.objects.exclude(branch=branch)
    
    context["other_departments"] = other_departments
    return JsonResponse(context)

  elif request.GET.get("list") == "other_subjects":
    other_subjects = Subject.objects.exclude(department__branch=branch)
    context["other_subjects"] = other_subjects
    return JsonResponse(context)

  elif request.GET.get("list") == "other_classes":
    other_classes = Class.objects.exclude(department__branch=branch)
    context["other_classes"] = other_classes
    return JsonResponse(context)

  elif request.GET.get("list") == "other_sections":
    other_sections = Section.objects.exclude(department__branch=branch)
    context["other_sections"] = other_sections
    return JsonResponse(context)

  elif request.GET.get("list") == "other_teachers":
    other_teachers = Teacher.objects.exclude(branchs=branch)
    context["other_teachers"] = other_teachers
    return JsonResponse(context)

  elif request.GET.get("list") == "other_students":
    other_students = []  
    for student in Student.objects.exclude(branch=branch):
      other_students.append({"id":student.id,"name":student.profile.user.get_full_name()})
                    
    context["objects"] = other_students
    return JsonResponse(context)

