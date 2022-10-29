from django.db import models
from django.core.validators import RegexValidator
from accounts.models import User
from academy.models import Section

# Create your models here.

#===========================================================================
class Student(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    admission_date = models.DateTimeField(auto_now_add=True)
    
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, null=True)
    
    #----------------------------------------
    sections = models.ManyToManyField(Section, blank=True)
    #----------------------------------------


    #------------------------------------------------------------------------------------
    PAYMENT_CHOICE = (
        ("unpaid", "UnPayed"),
        ("payed", "Payed"),
    )
    STATUS_CHOICE = (
        ("applied", "Applied"),
        ("pending", "Pending"),
        ("dismissed", "Dismissed"),
    )
    #------------------------------------------------------------------------------------

    payment = models.CharField(choices=PAYMENT_CHOICE, default="unpaid", max_length=10, null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICE,default="pending", max_length=10, null=True, blank=True)

    #------------------------------------------------------------------------------------

    class Meta:
        unique_together = ["user"]
        verbose_name = "student"
        ordering = ["-admission_date"]

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