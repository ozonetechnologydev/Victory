from django import forms

from teachers.models import Teacher

#===========================================================================
class AddTeacherForm(forms.ModelForm):
    phone_number = forms.RegexField(
        regex=r'^\+?1?\d{9,15}$', 
        widget = forms.TextInput(
            attrs={'class': 'form-control', 'type': 'tel',"placeholder":"Enter Phone number"}
        ),
    )
    class Meta:
        model = Teacher
        fields = ["user", "phone_number","profession", "educational_background",  "salary"]
        widgets = {
            
            "user": forms.Select(attrs={'class': 'form-control single-select'}),
            'profession': forms.TextInput(attrs={"class":"form-control","required":True, "placeholder":"Name",}),
            'passing_year': forms.DateInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Salary'}),
            'educational_background': forms.Textarea(attrs={"class":"form-control summernoteEditor", "rows":2, "placeholder":"bio body"}),
            
        }
#===========================================================================

