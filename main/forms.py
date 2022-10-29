from django import forms



from students.models import Student
from main.models import  File,Image
#===========================================================================


#===========================================================================
class ApplyStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [ "sections",]
        widgets = {
            #----------------------------------------
            'sections': forms.SelectMultiple(attrs={'class': 'multi-select'}),
            #----------------------------------------
        }


#===========================================================================
class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ["file",]
        widgets = {
            'file': forms.ClearableFileInput(attrs={'type':'file', 'name':'file','multiple':True}),
        }
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ["image",]
        widgets = {
            'file': forms.ClearableFileInput(attrs={'type':'file', 'name':'file','multiple':True}),
        }
