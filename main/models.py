from pydoc import describe
from turtle import width
from django.db import models
from django.core.validators import EmailValidator
from django.contrib.flatpages.models import FlatPage
from django.core.validators import RegexValidator


class GeneralSetting(models.Model):
    site_name = models.CharField(max_length=200, help_text="Enter your website name below")
    site_description = models.TextField(help_text="The site title might be the name of your company or organization, or a brief description of the organization, or a combination of the two.")
    logo=models.ImageField(upload_to="main/images", help_text="Upload your website logo - 120 x 40 ")
    favicon = models.ImageField(upload_to="main/images", help_text="Upload your website favicon - Standard for most desktop browsers. 32×32")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.site_name}'

class SocialNetwork(models.Model):
    name = models.CharField(max_length=200, help_text="this field can be Facebook Page ID, Twitter Username, YouTube Channel Name, Instagram Username and etc")
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.name}'
    
class PhoneNumber(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    number = models.CharField(validators=[phone_regex], max_length=17, null=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.number}'
    
    
class EmailAddress(models.Model):
    email_validator = EmailValidator()
    email = models.EmailField(validators = [email_validator])
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.email}'
    
#===========================================================================
class OfficeAddress(models.Model):
    office = models.CharField(max_length=200)
    street = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)

    #------------------------------------------------------------------------------------

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


class CoreValue(models.Model):
    title = models.CharField(max_length=200)
    descriptions = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.title}'
    
    
    
class Team(models.Model):
    team_name = models.CharField(max_length=200)
    users = models.ManyToManyField("accounts.User")
    created = models.DateTimeField(auto_now_add=True)
    descriptions = models.TextField(null=True, blank=True, help_text="brief description of the team,(this field can be markdown or HTML)")
    def __str__(self):
        return f'{self.team_name}'
    
    
    
    
class AboutUs(models.Model):
    title = models.CharField(max_length=200)
    descriptions = models.TextField(null=True, blank=True, help_text="brief description of the organization, or a combination of the two. (this field can be markdown or HTML)")
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.title}'
    
    
class Image(models.Model):
    image = models.ImageField(upload_to='blog/images', null=True, blank=True,)
    about = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.image.url}'
    
class File(models.Model):
    file = models.FileField(upload_to='blog/files', null=True, blank=True)
    about = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.file.url}'
    
class Gallery(models.Model):
    title = models.CharField(max_length=200)
    descriptions = models.TextField(null=True, blank=True, help_text="(this field can be markdown or HTML)")
    created = models.DateTimeField(auto_now_add=True)
    images = models.ManyToManyField(Image)



