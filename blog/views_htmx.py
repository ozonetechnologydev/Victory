from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse

from blog.models import Blog, BlogFile, BlogImage, BlogSubscriber
from home.forms import CommentForm
from home.models import Comment


def htmx_delete_blog_image(request, image_pk):
    image = BlogImage.objects.get(id=image_pk)
    image.delete()
    print(" image is deleted")
    return HttpResponse("")

def htmx_delete_blog_file(request, file_pk):
    file = BlogFile.objects.get(id=file_pk)
    file.delete()
    print(" file is deleted")
    return HttpResponse("")

def htmx_create_blog_comment(request, pk):
    blog = Blog.objects.get(id=pk)
    comment = Comment.objects.create(
        author = request.user,
        body_text = request.POST.get("body_text")
    )
    blog.comments.add(comment)
    blog.save()
    print("you create comment to the blog successfully")
    comment_form = CommentForm()
    context = {
        "blog":blog,
        "comments": blog.comments.all(),
        "comment_form":comment_form,
        "comment_form_action":f"/blog/htmx/{blog.id}/comment/create/",
    }
    return render(request, "components/comments.html", context)


def htmx_update_blog_comment(request, blog_pk, comment_pk ):
    blog = Blog.objects.get(id=blog_pk)
    comment = Comment.objects.get(id=comment_pk)
    comment_form = CommentForm(instance=comment)
    if request.method == "POST":
        comment_form = CommentForm(request.POST ,instance=comment)
        comment_form.save()
    print("you update comment to the blog successfully")
    context = {
        "blog":blog,
        "comments": blog.comments.all(),
        "comment_form":comment_form,
        "comment_form_action":f"/blog/htmx/{blog_pk}/comment/{comment_pk}/update/",
    }
    return render(request, "components/comments.html", context)

def htmx_create_blog_subscriber(request):
    context = {}
    subs = BlogSubscriber.objects.filter(email=request.POST.get("email"))
    if subs.exists():
        context["alert"]={"title":"Info","body":"You have already subscribed","type":"info",}
        print("you have already subscribed")
    else:
        try:
            print(request.POST.get("email"))
            BlogSubscriber.objects.create(email=request.POST.get("email"))
            context["alert"]={"title":"Success","body":"You have subscribed successfully","type":"success",}
            print("you have subscribed successfully")
            
        except:
            context["alert"]={"title":"Fail","body":"something is wronge please try again","type":"warning",}
            print("you have not subscribed successfully")
            
        
    return render(request, "components/alert.html", context)



