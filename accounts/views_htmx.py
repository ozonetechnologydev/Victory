from django.shortcuts import render, redirect,reverse
from django.http import HttpResponse
from accounts.forms import HtmxUserCreationForm, RegisterForm, updateUserForm
from django.contrib import messages
from accounts.models import User


from blog.models import BlogFile, BlogImage




# def htmx_create_user(request):
#   form = HtmxUserCreationForm()
#   if request.method == 'POST':
#     form = HtmxUserCreationForm(request.POST)
#     if form.is_valid():
#       print(form.fields)
      
#       first_name = request.POST.get('first_name')
#       last_name = request.POST.get('last_name')
#       email = request.POST.get('email')
#       password = request.POST.get('password')
      
#       user = User.object.create_user(
#           first_name = first_name,
#           last_name = last_name,
#           email = email,
#           password = password,
#       )
#       user.save()
#       messages.success(request, 'User is created successfully.')
#       print('Branch is created successfully.')
      
#     else:
#       print(form.errors)
#   else:
#     messages.info(request, 'You can add new user now')
  
#   context = {  
#     "form":form,
#     "show_messages":True,
#     "action":reverse("htmx_create_user"),
#   }
#   return render(request, "components/forms.html", context)
  
# def htmx_user_update(request, pk):
#   user = User.objects.get(id=pk)
#   form = HtmxUserCreationForm(instance=user)
#   if request.method == "POST":
#     form = HtmxUserCreationForm(request.POST, request.FILES, instance=user)
#     if form.is_valid():
#       user = form.save()
#       messages.success(request, 'Branch is =updated successfully.')
#       print('Branch is Updated successfully.')
#   else:
#     messages.info(request, 'You can update user new')
    
#   context = {  
#     "form":form,
#     "show_messages":True,
#     "action":f"/academy/htmx/user/{user.id}/update/",
#   }
#   return render(request, "components/forms.html", context)


def htmx_delete_user_image(request, pk):
    try:
      image = request.user.userimage_set.get(id=pk)
      image.delete()
    except:
      pass
    print(" image is deleted")
    return HttpResponse("")
  
def htmx_set_profile_image(request, pk):
    request.user.set_profile_image(pk)
    print(" image is profile")
    context = {
      "alert":{"title":"Success","body":"Image is set to profile successfully please refresh th page","type":"success",},
    }
    return render(request, "components/alert.html", context)
  
def htmx_set_cover_image(request, pk):
    request.user.set_cover_image(pk)
    print(" image is set cover")
    context = {
      "alert":{"title":"Success","body":"Image is set to profile successfully please refresh th page","type":"success",},
    }
    return render(request, "components/alert.html", context)

