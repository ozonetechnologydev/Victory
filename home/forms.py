from django import forms

from home.models import Comment, Contact, Review

#===========================================================================
class CreateContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["first_name", "last_name","email","phone_number","message"]
        widgets = {
            'first_name': forms.TextInput(attrs={"class":"form-control","required":True, "placeholder":"First Name",}),
            'last_name': forms.TextInput(attrs={"class":"form-control","required":True, "placeholder":"Last Name",}),
            'email': forms.EmailInput(attrs={"class":"form-control", "placeholder":"Enter Email"}),
            'phone_number': forms.TextInput(attrs={"class":"form-control","required":True,"type":"tel",}),
            'message': forms.Textarea(attrs={"class":"form-control ", "rows":5, "placeholder":"message body"}),
            
        }

#===========================================================================

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["rating","body_text"]
        widgets = {
            'rating': forms.NumberInput(attrs={"class":"form-range","required":True,"min":0, "max":5, "type":"range",}),
            'body_text': forms.Textarea(attrs={"class":"form-control ", "rows":5, "placeholder":"message body"}),
        }
        
#===========================================================================

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body_text",]
        widgets = {
            'body_text': forms.Textarea(
                attrs={
                    "class":"form-control border-0 form-control-simple no-resize", 
                    "rows":2, 
                    "placeholder":"Type a New Message"
                    }
                ),
        }