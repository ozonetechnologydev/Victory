
from django import forms
from academy.models import Branch, Department, Section
from students.models import Student
from django.db import models
from django.db.models import F, Q, Count, Prefetch



class NameModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f'{obj.name}'  
    

class NameModelMultipleChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f'{obj.name}'  
    
#===========================================================================
class ApplyStudentForm1(forms.ModelForm):
    phone_number = forms.RegexField(
        regex=r'^\+?1?\d{9,15}$', 
        widget = forms.TextInput(
            attrs={'class': 'form-control', 'type': 'tel',"placeholder":"Enter Phone number"}
        ),
    )
    class Meta:
        model = Student
        fields = ["phone_number"]
            #----------------------------------------
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'] = forms.ModelChoiceField(
            widget=forms.Select(attrs={'class': 'form-control single-select'}),
            queryset=Branch.objects.all(),
            required=False
        )

#===========================================================================
#===========================================================================
class ApplyStudentForm2(forms.ModelForm):
    class Meta:
        model = Section
        fields = ["department","level"]
        widgets = {
        }
    def __init__(self,branch_id = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        departments= Department.objects.all()
        if not branch_id in ['None', "", None]:
            departments=Department.objects.filter(
                branch__id=branch_id
            )        
            
        self.fields['department'] = NameModelChoiceField(
            widget=forms.Select(attrs={'class': 'form-control single-select'}),
            queryset=departments,
            required=False,
        )
        self.field_order = ['department', 'level']
    
        LEVEL_CHOICE = (
            ("beginner", "Beginner"),
            ("intermediate", "Intermediate"),
            ("advance", "Advance"),
        )
        
        self.fields['level'] = forms.ChoiceField(
            widget=forms.Select(attrs={'class': 'form-control single-select'}),
            choices=LEVEL_CHOICE,
            required=False
        )
        


#===========================================================================
class ApplyStudentForm3(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["sections"]
        
    def __init__(self, department_id = None,  level = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        sections = Section.objects.annotate(
                num_student = Count("student")
            ).filter(
                Q(num_student__lte = F("maximum_number_of_students"))
            )
            
        if not (department_id in ['None', "", None] or level in ['None', "", None]):
            
            sections = Section.objects.annotate(
                num_student = Count("student")
            ).filter(
                Q(num_student__lte = F("maximum_number_of_students")),
                department__id = department_id,
                level = level
            )
 
  
        
        self.fields['sections'] = NameModelMultipleChoiceField(
            widget=forms.SelectMultiple(attrs={'class': 'multi-select'}),
            queryset=sections,
            required=False,
            empty_label=None
        )

#===========================================================================



#===========================================================================
class HtmxAddStudentForm(forms.ModelForm):
    phone_number = forms.RegexField(
        regex=r'^\+?1?\d{9,15}$', 
        widget = forms.TextInput(
            attrs={'class': 'form-control', 'type': 'tel',"placeholder":"Enter Phone number"}
        ),
    )
    class Meta:
        model = Student
        fields = ["phone_number", "sections","status"]
        widgets = {
            #----------------------------------------
            'sections': forms.SelectMultiple(attrs={'class': 'multi-select',"required":False,}),
            'status':  forms.Select(attrs={'class': 'form-control single-select'}),
            #----------------------------------------
        }

#===========================================================================


#===========================================================================
class AddStudentForm(forms.ModelForm):
    phone_number = forms.RegexField(
        regex=r'^\+?1?\d{9,15}$', 
        widget = forms.TextInput(
            attrs={'class': 'form-control', 'type': 'tel',"placeholder":"Enter Phone number"}
        ),
    )
    class Meta:
        model = Student
        fields = ["user", "sections","phone_number"]
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control single-select',"placeholder":"Enter Phone number"}),

            #----------------------------------------
            'sections': forms.SelectMultiple(attrs={'class': 'multi-select',"required":False,}),
            #----------------------------------------
        }

#===========================================================================

