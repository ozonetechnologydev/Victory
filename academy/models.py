from email.policy import default
from django.db import models
from django.core.validators import MaxValueValidator


from datetime import datetime, timedelta
from home.models import Review
from main.models import  Image
from teachers.models import Teacher

#===========================================================================



# Create your models here.




#===========================================================================
class Branch(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=200, null=True, blank=True)
    #------------------------------------------------------------------------------------
    cover_image = models.ImageField(upload_to='academy/cover_image', default='academy/cover_image.jpg', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    descriptions = models.TextField(null=True, blank=True)
    reviews = models.ManyToManyField(Review, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    #------------------------------------------------------------------------------------
    class Meta:
     
        verbose_name = "branch"
        unique_together = ["name"]
        ordering = ["name"]

    #------------------------------------------------------------------------------------

    def natural_key(self):
        return {"name":self.name,}

    def __str__(self):
        return f"{self.name}"
#===========================================================================


#===========================================================================
class Department(models.Model):
    name = models.CharField(max_length=50)
    branch = models.ForeignKey(Branch,null=True, on_delete=models.CASCADE)

    #------------------------------------------------------------------------------------
    cover_image = models.ImageField(upload_to='academy/cover_image', default='academy/cover_image.jpg', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    descriptions = models.TextField(null=True, blank=True)
    reviews = models.ManyToManyField(Review, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    #------------------------------------------------------------------------------------

    class Meta:
    
        verbose_name = "department"
        unique_together = ["branch","name"]
        ordering = ["-created", "name"]

    #------------------------------------------------------------------------------------

    def natural_key(self):
        return {
            "name":self.name,
            "branch":self.branch,
        }
    def __str__(self):
        return f"{self.name} | {self.branch}"
#===========================================================================





#===========================================================================
class Subject(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department,null=True, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher,null=True, on_delete=models.CASCADE)
    reviews = models.ManyToManyField(Review, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    #------------------------------------------------------------------------------------
    cover_image = models.ImageField(upload_to='academy/cover_image', default='academy/cover_image.jpg', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    descriptions = models.TextField(null=True, blank=True)
    #------------------------------------------------------------------------------------
    class Meta:
        verbose_name = "subject"
        unique_together = ["department","name"]
        ordering = ["name"]

    #------------------------------------------------------------------------------------

    def natural_key(self):
        return {
            "name":self.name,
            "department":self.department,
        }
    def __str__(self):
        return f"{self.name} | {self.department}"
#===========================================================================


#===========================================================================
class Section(models.Model):
    name = models.CharField(max_length=20)
    shift_time = models.TimeField()
    department = models.ForeignKey(Department,null=True, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject)
    reviews = models.ManyToManyField(Review, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    maximum_number_of_students =models.PositiveSmallIntegerField(default=80, validators=[MaxValueValidator(100)])
        
    LEVEL_CHOICE = (
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advance", "Advance"),
    )
    level = models.CharField(choices=LEVEL_CHOICE, max_length=12)
    #------------------------------------------------------------------------------------
    cover_image = models.ImageField(upload_to='academy/cover_image', default='academy/cover_image.jpg', null=True, blank=True)
    descriptions = models.TextField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    #------------------------------------------------------------------------------------

    class Meta:
        verbose_name = "section"
        unique_together = ["department","name","shift_time"]
        ordering = ["name"]

    #----------------------------------------------------------------------------------

    def natural_key(self):
        return {
            "name":self.name,
            "department":self.department,
        }
        
    def get_students(self):
        return self.student_set
    
    
    def it_is_full(self):
        return self.maximum_number_of_students <= self.student_set.count()
    
    def __str__(self):
        return f"{self.name} | shift-{self.shift_time} | {self.level} | {self.department}"
#===========================================================================

