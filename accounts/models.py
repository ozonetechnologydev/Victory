from datetime import datetime, timedelta
from email.policy import default
from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import EmailValidator
# Create your models here.
from django.contrib.auth.models import AbstractUser


from main.models import Image
#===========================================================================


#===========================================================================
class User(AbstractUser):
    # mother_name = models.CharField(max_length=50)
    username_validator = UnicodeUsernameValidator()
    email_validator = EmailValidator()
    #------------------------------------------------------------------------------------
    about = models.TextField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    birth_date = models.DateField(null=True)
    email = models.EmailField(unique=True, validators = [email_validator])
    username = models.CharField(
        max_length=191,
        validators = [username_validator],
        help_text="Required. 150 characters or fewer. Usernames may contain alphanumeric, _, @, +, . and - characters.", 
        unique=True,null=True, blank=True
    )
    #------------------------------------------------------------------------------------
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']
    #------------------------------------------------------------------------------------
    GENDER_CHOICE = (
        ("male", "Male"),
        ("female", "Female"),
    )
    gender = models.CharField(choices=GENDER_CHOICE, max_length=10)
    #------------------------------------------------------------------------------------
    def is_academic_registrar(self):
        academic_registrar_permissions = [
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
        ]
        all_user_perms =  list(self.get_all_permissions())
        has_num_parm = 0
        for perms in academic_registrar_permissions:
          if perms in all_user_perms:
            has_num_parm += 1
        if has_num_parm == len(academic_registrar_permissions):
          return True
        else:
          return False

    
    def is_student_registrar(self):
        student_registrar_permissions = [
            "accounts.add_user",
            "accounts.change_user",
            "accounts.delete_user",
            
            "students.add_student",
            "students.change_student",
            "students.delete_student",
        ]
        all_user_perms =  list(self.get_all_permissions())
        has_num_parm = 0
        for perms in student_registrar_permissions:
          if perms in all_user_perms:
            has_num_parm += 1
        if has_num_parm == len(student_registrar_permissions):
          return True
        else:
          return False
      
      
    def get_full_name_or_email(self):
        full_name = self.get_full_name()
        return full_name if full_name!="" else self.email
    
    
    def is_blog_publisher(self):
        blog_publisher = [
            "blog.add_blog",
            "blog.change_blog",
            "blog.delete_blog",
            
            "blog.can_publish",
            "blog.can_unpublish",
        ]
        all_user_perms =  list(self.get_all_permissions())
        has_num_parm = 0
        for perms in blog_publisher:
          if perms in all_user_perms:
            has_num_parm += 1
        if has_num_parm == len(blog_publisher):
          return True
        else:
          return False
      
      
    
    def get_age(self):
        today = datetime.today()
        age = today - self.birth_date
        return f"{age}"
    
    def get_profile_images(self):
        image = self.userimage_set.filter(role = "profile_image")
        return image        
    
    def get_cover_images(self):
        image = self.userimage_set.filter(role = "cover_image")
        return image        
    
    
    def get_gallery_images(self):
        image = self.userimage_set.filter(role = "gallery_image")
        return image        

    #------------------------------------------------------------------------------------
    def get_profile_image(self):
        image = self.userimage_set.order_by("-updated", "-created").filter(role = "profile_image")
        if image.exists():
            return image.first().image
        else:
            return None

    def get_cover_image(self):
        image = self.userimage_set.order_by("-updated", "-created").filter(role = "cover_image")
        if image.exists():
            return image.first().image
        else:
            return None

    #------------------------------------------------------------------------------------
    def set_profile_image(self, pk):
        image = self.userimage_set.get(id=pk)
        image.role = "profile_image"
        image.save()
        return image
    
    def set_cover_image(self, pk):
        image = self.userimage_set.get(id=pk)
        image.role = "cover_image"
        image.save()
        return image
    #------------------------------------------------------------------------------------

    class Meta:
        verbose_name = "user"
        ordering = ["-date_joined"]

    #----------------------------------------------------------------------------------

    def natural_key(self):
        return {
            "full_name":self.get_full_name(),
            "email":self.email,
        }
    def __str__(self):
        return f"{self.get_full_name()}" if self.get_full_name() else  f"{self.email}"
#===========================================================================


#===========================================================================
class Address(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    street = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)

    #--------------------------/----------------------------------------------------------

    class Meta:
        verbose_name = "address"

    #----------------------------------------------------------------------------------

    def natural_key(self):
        return {
            "street":self.street, "city":self.city, "state":self.state
        }
    def __str__(self):
        return f"{self.street} | {self.city} | {self.state}"
#===========================================================================



class UserImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user/images')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    about = models.TextField(null=True, blank=True)
    ROLE_CHOICE = (
        ("profile_image", "Profile Image"),
        ("cover_image", "Cover Image"),
        ("gallery_image", "Gallery Image"),
    )
    role = models.CharField(choices=ROLE_CHOICE, default="gallery_image", max_length=15)
    def __str__(self):
        return f'{self.image}'
    
    #------------------------------------------------------------------------------------

    class Meta:
        ordering = ["-updated", "-created"]
