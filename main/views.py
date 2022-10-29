from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from main.decorators import admin_only


from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage

from main.models import Image, File

from main.forms import FileForm, ImageForm
from academy.models import Branch , Department, Subject, Section
from accounts.models import User
from teachers.models import Teacher
from students.models import Student
#===========================================================================







#===========================================================================
@admin_only
@login_required(login_url='login')
def users_dashboard(request):
    total_num_students = Student.objects.count()
    total_num_teachers = Teacher.objects.count()
    
    total_num_users = User.objects.count()
    total_num_admins = User.objects.filter(is_superuser=True).count()

    new_users_list = User.objects.order_by("-date_joined")[:10]
    
      
    students_num = Student.objects.count()
    students_num_male = Student.objects.filter(user__gender__istartswith = "male").count()
    students_num_female = Student.objects.filter(user__gender__istartswith = "Female").count()  
    
    teachers_num_male = Teacher.objects.filter(user__gender__istartswith = "male").count()
    teachers_num_female = Teacher.objects.filter(user__gender__istartswith = "Female").count()
    teachers_num = Teacher.objects.count()

    new_students_last = Student.objects.order_by("-user__user__date_joined")[:10]
    new_teachers_last =  Teacher.objects.order_by("-user__user__date_joined")[:10]

    context = {
        "total_num_students":total_num_students,
        "total_num_teachers":total_num_teachers,
        "total_num_users":total_num_users,
        "total_num_admins":total_num_admins,
        "new_users_list":new_users_list,

        "students_num":students_num, 
        "students_num_male":students_num_male,
        "students_num_female":students_num_female,
        "new_students_last":new_students_last, 

        "teachers_num": teachers_num, 
        "teachers_num_male":teachers_num_male,
        "teachers_num_female":teachers_num_female,
        "new_teachers_last": new_teachers_last, 
    }
    return render(request, "users/admin/users_dashboard.html", context)
#===========================================================================





#===========================================================================


def test_url(request):
  print(request.POST)
  print(request.FILES)
  context= {}
  return render(request, "test/test.html", context)

def upload_file(request):
  # print(request.FILES.getlist("file"))
  context = []
  file = request.FILES.get("file")
  
  if file.content_type.split("/")[0] == "image":
    image = Image.objects.create(image=file)
    context = {
        "image_url":image.image.url,
        "image_id":image.id
      }
  
  else:
    file = File.objects.create(file=file)
    context = {
        "file_url":file.file.url,
        "file_id":file.id
      }
    

  return JsonResponse(context)



def delete_image(request, pk):
  image = Image.objects.get(id=pk)
  image.delete()
  print(" image is deleted")
  return HttpResponse("")

def delete_file(request, pk):
  file = File.objects.get(id=pk)
  file.delete()
  print(" file is deleted")
  
  return HttpResponse("")


