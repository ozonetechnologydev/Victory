import email
from django.db import models

# Create your models here.
from datetime import datetime


from accounts.models import User
from home.models import Comment, Review, View


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, help_text="Field must contain an unique value")
    descriptions = models.TextField(null=True, blank=True)
    #------------------------------------------------------------------------------------
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    #------------------------------------------------------------------------------------
    def get_blogs(self):
        return self.blog_set.all()
       
    def get_published_blogs(self):
        return self.blog_set.filter(status="published")
    
    def __str__(self):
        return f'{self.title}'
    


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,blank=True)
    title = models.CharField(max_length=255, null=True,blank=True)
    body_text = models.TextField(null=True, blank=True)
    #------------------------------------------------------------------------------------
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(null=True,blank=True)
    #------------------------------------------------------------------------------------
    comments = models.ManyToManyField(Comment, blank=True)
    views = models.ManyToManyField(View, blank=True)
    pin_to_top = models.BooleanField(default=False)
    #------------------------------------------------------------------------------------
    
    STATUS_CHOICE = (
        ("published", "Published"),
        ("scheduled", "Scheduled"),
        ("draft", "Draft"),
        ("deleted", "Deleted"),
    )
    status = models.CharField(choices=STATUS_CHOICE,default="draft", max_length=20, null=True, blank=True)
    #------------------------------------------------------------------------------------
    coped_from = models.ForeignKey("blog.Blog", on_delete=models.SET_NULL, null=True, blank=True)
    #------------------------------------------------------------------------------------
    
    
    class Meta:
        verbose_name = "blog"
        ordering = ["-published","-updated","-created"]

    #----------------------------------------------------------------------------------
    def get_images(self):
        return self.blogimages_set.all()
        
    def get_files(self):
        return self.blogfiles_set.all()
        
    #----------------------------------------------------------------------------------
    def delete_blog(self):
        self.status = "deleted"
        self.save()
        
    def publish_blog(self):
        self.published = datetime.now()
        self.status = "published"
        self.save()
        
    def unpublish_blog(self):
        self.status = "draft"
        self.save()
        
    #----------------------------------------------------------------------------------

    def natural_key(self):
        return {
            "author":self.author.get_full_name(),
            "title":self.title,
        }

    def __str__(self):
        return f"{self.title}"
    


class BlogImage(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog/images')
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.image}'
    
class BlogFile(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    file = models.FileField(upload_to='blog/files')
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.file}'
    


class BlogSubscriber(models.Model):
    email = models.EmailField(unique=True)
    def __str__(self):
        return f'{self.email}'
    