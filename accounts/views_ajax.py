from django.http import HttpResponse, HttpResponseNotModified
from django.http import JsonResponse
from django.urls import reverse

from accounts.models import User, UserImage




def ajax_upload_user_profile_image(request):
    new_file = request.FILES.get("file")
    context = {"success":False}
    if new_file.content_type.split("/")[0] == "image":
        image = request.user.userimage_set.create(image=new_file, role="profile_image")
        context = {
            "success":True,
            "file_name":f"{new_file}",
            "file_view_url":image.image.url,
            "file_delete_url":f"/accounts/ajax/image/{image.id}/delete/" 
        }
        print(context)
    else:
        return HttpResponseNotModified()
            
        
    return JsonResponse(context)

def ajax_upload_user_cover_image(request):
    new_file = request.FILES.get("file")
    context = {"success":False}
    if not new_file in ["null", "Null", None, 'None', ''] and new_file.content_type.split("/")[0] == "image":
        image = request.user.userimage_set.create(image=new_file, role="cover_image")
        context = {
            "success":True,
            "file_name":f"{new_file}",
            "file_view_url":image.image.url,
            "file_delete_url":f"/accounts/ajax/image/{image.id}/delete/" 
        }
        print(context)
    else:
        return HttpResponseNotModified()
            
        
    return JsonResponse(context)

def ajax_upload_user__gallery_image(request):
    new_file = request.FILES.get("file")
    context = {"success":False}
    if new_file.content_type.split("/")[0] == "image":
        image = request.user.userimage_set.create(image=new_file, role="gallery_image")
        context = {
            "success":True,
            "file_name":f"{new_file}",
            "file_view_url":image.image.url,
            "file_delete_url":f"/accounts/ajax/image/{image.id}/delete/" 
        }
        print(context)
    else:
        return HttpResponseNotModified()
            
        
    return JsonResponse(context)


def ajax_delete_user_image(request, pk):
  image = request.user.userimage_set.get(id = pk) 
  image.delete()
  print(" image is deleted")
  
  return JsonResponse({"result":"successfully deleted"})

