from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse

from blog.forms import BlogFileForm, BlogImageForm
from blog.models import Blog, BlogFile, BlogImage




def ajax_upload_blog_file(request, blog_pk):
    blog = Blog.objects.get(id=blog_pk)
    new_file = request.FILES.get("file")

    context = {"success":False}
    if new_file.content_type.split("/")[0] == "image":
        image = blog.blogimage_set.create(image=new_file)
        context = {
            "success":True,
            "file_name":f"{new_file}",
            "file_view_url":image.image.url,
            "file_delete_url":f"/blog/ajax/files/{image.id}/delete_image/" 
        }
    else:
        file = blog.blogfile_set.create(file=new_file)
        context = {
            "success":True,
            "file_name":f"{new_file}",
            "file_view_url":file.file.url,
            "file_delete_url":f"/blog/ajax/files/{file.id}/delete_file/" 
        }
        
    return JsonResponse(context)



def ajax_delete_blog_image(request, image_pk):
  image = BlogImage.objects.get(id=image_pk)
  image.delete()
  print(" image is deleted")
  
  return JsonResponse({"result":"successfully deleted"})

def ajax_delete_blog_file(request, file_pk):
  file = BlogFile.objects.get(id=file_pk)
  file.delete()
  print(" file is deleted")
  
  return JsonResponse({"result":"successfully deleted"})

