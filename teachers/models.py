from django.db import models
from django.core.validators import RegexValidator


from accounts.models import  User
from home.models import  Review


# Create your models here.
#===========================================================================
class Teacher(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    joining_date = models.DateTimeField(auto_now_add=True)
    educational_background = models.TextField(null=True, blank=True)
    profession = models.CharField(max_length=250, null=True, blank=True)
    reviews = models.ManyToManyField(Review, blank=True)
    #----------------------------------------
    salary = models.IntegerField(null=True, blank=True)
    #------------------------------------------------------------------------------------
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, null=True)
    
    class Meta:
        unique_together = ["user"]
        verbose_name = "teacher"
        ordering = ["-joining_date"]

    #----------------------------------------------------------------------------------

    def natural_key(self):
        return {
            "name":self.user.get_full_name(),
            "email":self.user.email,
            "username":self.user.username,
        }

    def __str__(self):
        return f"{self.user.get_full_name()}"
#===========================================================================