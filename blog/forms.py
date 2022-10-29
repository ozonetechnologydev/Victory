
from django import forms
from blog.models import Blog, BlogFile, BlogImage, Category



#===========================================================================
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["title",'slug','descriptions']
        widgets = {
            'title': forms.TextInput(attrs={"class":"form-control","required":True, "placeholder":"Title",}),
            'body_text': forms.Textarea(attrs={"class":"form-control w-100", "placeholder":"descriptions body"}),
            'slug': forms.TextInput(attrs={"class":"form-control","required":True, "placeholder":"https://example.com/",}),
        }
        
#===========================================================================
class AddBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','category', 'published', 'body_text','status','pin_to_top']
        widgets = {
            'title': forms.TextInput(attrs={"class":"form-control","required":True,"autofocus":True, "placeholder":"Title",}),
            'published': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'body_text': forms.Textarea(attrs={"class":"form-control summernoteEditor", "placeholder":"blog body"}),
            'category': forms.Select(attrs={"class":"form-control single-select","required":True}),
            'status': forms.Select(attrs={"class":"form-control single-select","required":True}),
            'pin_to_top': forms.CheckboxInput(attrs={"class":"inline-success"}),
        }


#===========================================================================
class BlogFileForm(forms.ModelForm):
    class Meta:
        model = BlogFile
        fields = ['file', 'blog']
        
        
#===========================================================================



class BlogImageForm(forms.ModelForm):
    class Meta:
        model = BlogImage
        fields = ['image', 'blog']
