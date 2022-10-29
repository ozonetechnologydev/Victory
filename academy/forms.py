from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django import forms
from .models import (Branch, Department, Subject, Section)
#===========================================================================



class NameModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return f'{obj.name}'    

class NameModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f'{obj.name}' 

class HtmxCreateBranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['name','location',]
        widgets = {
            'name': forms.TextInput(attrs={"class":"form-control","required":True, "placeholder":"Name",}),
            'location': forms.TextInput(attrs={"class":"form-control","required":True, "placeholder":"State",}),
        }





class HtmxCreateDepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name',]
        widgets = {
            'name': forms.TextInput(attrs={"class":"form-control","required":True, "placeholder":"Name",}),
        }


class HtmxCreateSubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name','teacher',  ]
        widgets = {
            'name': forms.TextInput(attrs={"class":"form-control","required":True, "placeholder":"Name",}),
            "teacher": forms.Select(attrs={'class': 'form-control single-select'}),
        }
        
    def clean_name_and_department(self,name, department):

        if Subject.objects.filter(name__iexact = name,  department=department).exists():
            self.add_error("name", f" '{name}' with '{department.name}' is already exist!") 
        
        
    def __init__(self, branch_id = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if not branch_id in [None, 'None',  '', 'none', 'null']:
            
            departments = Department.objects.filter(branch__id = branch_id)
            self.fields['department'] = NameModelChoiceField(
                widget=forms.Select(attrs={'class': 'form-control single-select'}),
                queryset=departments,
                required=True,
                empty_label=None
            )
        

        
class HtmxCreateSectionForm(forms.ModelForm):
    
    class Meta:
        model = Section
        fields = ['name',  'shift_time','level','subjects','maximum_number_of_students']
        widgets = {
            'name': forms.TextInput(attrs={"class":"form-control","required":True, "placeholder":"Name",}),
            #----------------------------------------
            "subjects": forms.SelectMultiple(attrs={'class': 'multi-select'}),
            #----------------------------------------
            'shift_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            "level": forms.Select(attrs={'class': 'form-control single-select'}),
            'maximum_number_of_students':forms.NumberInput(attrs={"class":"form-control", "placeholder":"maximum_number_of_students"}),
            
        }
    
    
    def clean_name_and_department(self,name,shift_time, department):

        if Section.objects.filter(name__iexact = name, shift_time=shift_time,  department=department).exists():
            self.add_error("name", f" '{name} with '{department.name}' is already exist!") 
            self.add_error("shift_time", f" '{shift_time}' with '{department.name}' is already exist!") 
            
            
            
    def __init__(self, branch_id = None, department_id = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        subjects = Subject.objects.all()
        UseModelMultipleChoiceField = forms.ModelMultipleChoiceField
        if not branch_id in [None, 'None',  '', 'none', 'null']:
            subjects = Subject.objects.filter(department__branch__id = branch_id)
            
            departments = Department.objects.filter(branch__id = branch_id)
            self.fields['department'] = NameModelChoiceField(
                widget=forms.Select(attrs={'class': 'form-control single-select'}),
                queryset=departments,
                required=True,
                empty_label=None
            )
            self.order_fields(['name', 'department' ,'shift_time','level','subjects','maximum_number_of_students'])
            
        if not department_id in [None, 'None',  '', 'none', 'null']:
            subjects = Subject.objects.filter(department__id = department_id)
            UseModelMultipleChoiceField = NameModelMultipleChoiceField
            
        self.fields['subjects'] = UseModelMultipleChoiceField(
            widget=forms.SelectMultiple(attrs={'class': 'multi-select'}),
            queryset=subjects,
            required=True,
        )
        
        
        
#===========================================================================
class CreateBranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['name','location',]
        widgets = {
            'name': forms.TextInput(attrs={"class":"form-control","required":True, "placeholder":"Name",}),
            'location': forms.TextInput(attrs={"class":"form-control","required":True, "placeholder":"State",}),
        }
#===========================================================================
class UpdateBranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['name','location', 'cover_image', 'bio', 'descriptions']
        widgets = {
            'name': forms.TextInput(attrs={"class":"form-control","required":True, "placeholder":"Name",}),
            'location': forms.TextInput(attrs={"class":"form-control","required":True, "placeholder":"State",}),
            'descriptions': forms.Textarea(attrs={"class":"form-control summernoteEditor", "placeholder":"Descriptions body"}),
            'cover_image': forms.FileInput(attrs={"class":"form-control ","placeholder":"Enter Username"}),
            'bio': forms.Textarea(attrs={"class":"form-control",  "rows":5, "placeholder":"bio.."}),

        }
#===========================================================================



#===========================================================================
class CreateDepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'branch']
        widgets = {
            'name': forms.TextInput(attrs={"class":"form-control","required":True, "placeholder":"Name",}),
            "branch": forms.Select(attrs={'class': 'form-control single-select'}),
        }
#===========================================================================
class UpdateDepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name','cover_image', 'branch', 'bio', 'descriptions']
        widgets = {
            'name': forms.TextInput(attrs={"class":"form-control","required":True, "placeholder":"Name",}),
            "branch": forms.Select(attrs={'class': 'form-control single-select'}),
            'descriptions': forms.Textarea(attrs={"class":"form-control summernoteEditor", "placeholder":"Descriptions body"}),
            'cover_image': forms.FileInput(attrs={"class":"form-control ","placeholder":"Enter Username"}),
            'bio': forms.Textarea(attrs={"class":"form-control",  "rows":5, "placeholder":"bio.."}),

        }
#===========================================================================


#===========================================================================
class CreateSubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name','department','teacher', ]
        widgets = {
            'name': forms.TextInput(attrs={"class":"form-control","required":True, "placeholder":"Name",}),
            "department": forms.Select(attrs={'class': 'form-control single-select'}),
            "teacher": forms.Select(attrs={'class': 'form-control single-select'}),
        }
#===========================================================================
class UpdateSubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name','cover_image','department','teacher',  'bio',  'descriptions']
        widgets = {
            'name': forms.TextInput(attrs={"class":"form-control","required":True, "placeholder":"Name",}),
            "department": forms.Select(attrs={'class': 'form-control single-select'}),
            "teacher": forms.Select(attrs={'class': 'form-control single-select'}),
            'descriptions': forms.Textarea(attrs={"class":"form-control summernoteEditor", "placeholder":"Descriptions body"}),
            'cover_image': forms.FileInput(attrs={"class":"form-control  ","placeholder":"Enter Username"}),
            'bio': forms.Textarea(attrs={"class":"form-control",  "rows":5, "placeholder":"bio.."}),

        }
#===========================================================================


#===========================================================================
class CreateSectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['name','department', 'subjects', 'shift_time','level','maximum_number_of_students']
        widgets = {
            'name': forms.TextInput(attrs={"class":"form-control","required":True, "placeholder":"Name",}),
            #----------------------------------------
            'department': forms.Select(attrs={'class': 'form-control single-select'}),
            "subjects": forms.SelectMultiple(attrs={'class': 'multi-select'}),
            #----------------------------------------
            'shift_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            "level": forms.Select(attrs={'class': 'form-control single-select'}),
            'maximum_number_of_students':forms.NumberInput(attrs={"class":"form-control", "placeholder":"maximum_number_of_students"}),
            
        }
#===========================================================================
class UpdateSectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['name','cover_image','department', 'subjects', 'shift_time','bio',"level", 'maximum_number_of_students', 'descriptions']
        widgets = {
            'name': forms.TextInput(attrs={"class":"form-control","required":True, "placeholder":"Name",}),
            'cover_image': forms.FileInput(attrs={"class":"form-control  ","placeholder":"Enter Username"}),
            #----------------------------------------
            'department': forms.Select(attrs={'class': 'form-control single-select'}),
            "subjects": forms.SelectMultiple(attrs={'class': 'multi-select'}),
            #----------------------------------------
            'shift_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'descriptions': forms.Textarea(attrs={"class":"form-control summernoteEditor", "placeholder":"Descriptions body"}),
            'bio': forms.Textarea(attrs={"class":"form-control",  "rows":5, "placeholder":"bio.."}),
            "level": forms.Select(attrs={'class': 'form-control single-select'}),
            'maximum_number_of_students':forms.NumberInput(attrs={"class":"form-control", "placeholder":"maximum_number_of_students"}),
            

        }
#===========================================================================
