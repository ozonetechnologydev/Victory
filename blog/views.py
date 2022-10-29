from datetime import datetime, timedelta, date
from django.utils import timezone
import pytz
from django.core.paginator import Paginator
from genericpath import exists
from unicodedata import category
from django.shortcuts import render,redirect, reverse
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from django import forms



from django.core.mail import send_mail, send_mass_mail


from blog.forms import AddBlogForm, CategoryForm
from blog.models import Blog, BlogFile, BlogImage, Category, BlogSubscriber
from home.forms import CommentForm
# Create your views here.

from main.models import Image, File
from home.models import Comment, View




def blog_list(request):
    blogs = Blog.objects.order_by("-published").filter(status="published").exclude(category=None)
    
    if request.GET.get("search"):
        search =  request.GET.get("search")
        print(search)
        blogs = Blog.objects.order_by("-published").filter(
            Q(category__title__icontains= search) |
            Q(title__icontains = search),
            status="published"
        )
        
        
    if request.GET.get("category") and request.GET.get("category") != "all":
        category =  request.GET.get("category")
        blogs = Blog.objects.order_by("-published").filter(category__title = category, status="published")
    
    if request.GET.get("date"):
        dateFilter =  request.GET.get("date")
        year, month = dateFilter.split("-")
        blogs = Blog.objects.order_by("-published").filter(
            published__gt = datetime(int(year), int(month), 1, tzinfo=pytz.UTC), 
            published__lte = datetime(int(year), int(month), 31, tzinfo=pytz.UTC), 
            status="published")
        print("int is working")
 
        
    pin_blogs = Blog.objects.order_by("-published").filter(status="published", pin_to_top=True).exclude(category=None)
        
    archives = Blog.objects.dates('published', 'month')
    blog_last = Blog.objects.order_by("-published").filter(status="published").exclude(category=None).first()
    recent_blog = Blog.objects.order_by("-published").filter(status="published").exclude(category=None)[:5]
    categories = Category.objects.filter(blog__status="published")
    
    paginator = Paginator(blogs, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        "page_obj":page_obj,
        "pin_blogs":pin_blogs,
        "categories":categories,
        "recent_blog":recent_blog,
        "blog_last":blog_last,
        'archives':archives,
    }    
    
    if request.GET.get('page'):
        return render(request, "components/blog_lists.html", {"page_obj":page_obj,}) 
    return render(request, "blog/public/blog.html", context)

def blog_details(request, pk):
    
    blog = Blog.objects.get(id = pk)
    related_blogs = Blog.objects.filter(category = blog.category)
    img_len = blog.blogimage_set.count()
    
    blog_image_col_1 = blog.blogimage_set.all()[:int(img_len/3)]
    blog_image_col_2 = blog.blogimage_set.all()[int(img_len/3):int(img_len*(2/3))]
    blog_image_col_3 = blog.blogimage_set.all()[int(img_len*(2/3)):]
    
    
    
    views= blog.views.filter(author=request.user)
    print(views.exists())
    if not views.exists():
        view = View.objects.create(author=request.user)
        blog.views.add(view)
        blog.save()
        
    paginator = Paginator(related_blogs, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    comment_form = CommentForm()
    context = {
        "blog":blog,
        "page_obj":page_obj,
        "blog_image_col_1": blog_image_col_1,
        "blog_image_col_2": blog_image_col_2,
        "blog_image_col_3":blog_image_col_3,
        "comment_form":comment_form,
        "comment_form_action":f"/blog/htmx/{blog.id}/comment/create/",
    } 
    if request.GET.get('page'):
        return render(request, "components/blog_lists.html", {"page_obj":page_obj,})
    # if request.user.is_superuser:
    #     return render(request, "blog/admin/admin_blog_details.html", context)   
    
    return render(request, "blog/public/blog_details.html", context)



def admin_create_blog(request):
    blog, created = Blog.objects.get_or_create(
        author=request.user,
        category = None,
        title = None,
        body_text = None,
        created = None,
        updated = None,
        published = None,
        status = None,
    )
    if created:
        return redirect("admin_update_blog",blog.id)
    else:
        return redirect("admin_update_blog",blog.last().id)
        
def admin_duplicate_blog(request, pk):
    blog = Blog.objects.get(id=pk)
    new_blog = Blog.objects.create(
        author=request.user,
        category = blog.category,
        title = blog.title,
        body_text = blog.body_text,
        status = blog.status,
        coped_from=blog,
    )
    for file in blog.blogfile_set.all():
        new_blog.blogfile_set.create(file__url=file.file.url)
        
    for image in blog.blogfile_set.all():
        new_blog.blogimage_set.create(image__url=image.image.url)
    
    
    return redirect("admin_update_blog", new_blog.id)



def admin_update_blog(request, pk):
    
    blog = Blog.objects.get(id=pk)
    print(blog.coped_from)
    if blog.coped_from != None:
       messages.success(request, 'Your have been duplicated the blog successfully.')
        
    form = AddBlogForm(instance=blog)
    print(request.META.get("HTTP_REFERER"))
    if request.method == "POST":
        form = AddBlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            print(request.POST)
            return redirect("blog_details", blog.id)

    
    context = {"form": form, "blog": blog}      
    return render(request, "blog/admin/admin_blog_create_and_update.html", context)

def admin_publish_blog(request, pk):
    blog = Blog.objects.get(id=pk)
    blog.publish_blog()
    
    mail_recipient_list = []
    for obj in BlogSubscriber.objects.values('email'):
        mail_recipient_list.append(obj["email"])
        
    admin_details_blog_url = reverse("admin_details_blog", blog.id)
    send_mail(
        "new Blog",
        "this is new blog",
        html_message=f"<a href='{admin_details_blog_url}' newtab>{blog.title}</a>",
        recipient_list=mail_recipient_list,
        fail_silently=True
    )
    
    redirect_to = request.META.get("HTTP_REFERER")
    if redirect_to == None:
        redirect_to = "admin_blog_list"
    return redirect(redirect_to)

def admin_unpublish_blog(request, pk):
    blog = Blog.objects.get(id=pk)
    blog.unpublish_blog()
    redirect_to = request.META.get("HTTP_REFERER")
    if redirect_to == None:
        redirect_to = "admin_blog_list"
    return redirect(redirect_to)

def admin_delete_blog(request, pk):
    blog = Blog.objects.get(id=pk)
    blog.delete_blog()
    redirect_to = request.META.get("HTTP_REFERER")
    if redirect_to == None:
        redirect_to = "admin_blog_list"
    return redirect(redirect_to)



def admin_blog_overview(request):
    today = datetime.today()
    last_30_day = today - timedelta(days=30)
    num_all_blogs = Blog.objects.order_by("-created").count()
    num_bogs_last_30_day = Blog.objects.order_by("-created").filter(created__lte = today, created__gt= last_30_day).count()
   
    num_all_blogs_medias = BlogFile.objects.select_related("blog").count()
    num_all_blogs_assets = BlogImage.objects.select_related("blog").count() + num_all_blogs_medias
    
    num_comment_for_all_before_tody_blogs = Comment.objects.select_related("blog").filter(created=today - timedelta(days=1)).count()
    num_comment_for_today_blogs = Comment.objects.select_related("blog").filter(created=today).count()
    num_all_views_for_last_30_day_blogs = View.objects.select_related("blog").filter(created__lte = today, created__gt= last_30_day).count()
    num_all_views_blogs = View.objects.select_related("blog").count()
    
    
    recent_blog = Blog.objects.order_by("-created")[:10]
    
    context = {
        "num_all_blogs":num_all_blogs,
        "recent_blog":recent_blog,
        "num_bogs_last_30_day":num_bogs_last_30_day,
        "num_comment_for_today_blogs":num_comment_for_today_blogs,
        "num_all_blogs_medias":num_all_blogs_medias,
        "num_all_blogs_assets":num_all_blogs_assets,
        "num_comment_for_all_before_tody_blogs":num_comment_for_all_before_tody_blogs,
        "num_all_views_for_last_30_day_blogs":num_all_views_for_last_30_day_blogs,
        "num_all_views_blogs":num_all_views_blogs,
    }    
    return render(request, "blog/admin/admin_blog_overview.html", context)

def admin_blog_list(request):
    blogs = Blog.objects.order_by("-created")
    if request.GET.get("category") and request.GET.get("category") != "all":
        category =  request.GET.get("category")
        blogs = Blog.objects.order_by("-created").filter(category__name = category)
        

    blog_last = Blog.objects.order_by("-created").first()
    recent_blog = Blog.objects.order_by("-created")[:5]
    categories = Category.objects.exclude(blog=None)
    context = {
        "blogs":blogs,
        "categories":categories,
        "recent_blog":recent_blog,
        "blog_last":blog_last,
    }    
    return render(request, "blog/admin/admin_blog_list.html", context)


def admin_blog_create_category(request):
    form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'category is created successfully.')
            form = CategoryForm()
            context = {
                "form":form,
                "show_messages":True,
            } 
            return render(request, "components/form.html", context)
    context = {
        "form":form,
    }    
    return render(request, "components/form.html", context)

def admin_blog_category(request):
    categories = Category.objects.order_by("-created")
    context = {
        "categories":categories,
    }    
    return render(request, "blog/admin/admin_blog_category.html", context)

def admin_blog_update_category(request,pk):
    category = Category.objects.get(id=pk)
    form = CategoryForm(instance=category)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'category is updated successfully.')
            form = CategoryForm(instance=category)
            context = {
                "form":form,
                "show_messages":True,
            } 
            return render(request, "components/form.html", context)
    context = {
        "form":form,
    }    
    return render(request, "components/form.html", context)

def admin_blog_delete_category(request, pk):
    categories = Category.objects.order_by("-created")
    context = {
        "categories":categories,
    }    
    return render(request, "blog/admin/admin_blog_category.html", context)