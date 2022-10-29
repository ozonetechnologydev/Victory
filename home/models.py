from django.db import models


from accounts.models import User



class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    #------------------------------------------------------------------------------------
    created = models.DateTimeField(auto_now_add=True)
    body_text = models.TextField(null=True, blank=True)
    #------------------------------------------------------------------------------------
    class Meta:
        ordering = ["-created"]
        
    def __str__(self):
        return f"{self.author} => {self.body_text}" 

    

class Comment(models.Model):
    author = models.ForeignKey(User,  on_delete=models.CASCADE)
    body_text = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    reply = models.ForeignKey("home.Comment",related_name="reply_to", on_delete=models.SET_NULL, null=True, blank=True)
    forward = models.ForeignKey("home.Comment",related_name="forward_from", on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        ordering = ["-created"]
    
    def __str__(self):
        return f'{self.author}, {self.created}'
 
class View(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)   
    def __str__(self):
        return f'{self.author}, {self.created}'
    
    
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    message = models.TextField(null=True, blank=True)
    date_time = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-created"]
        
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
