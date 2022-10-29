from django import forms
WIDGETS = {
    'password': forms.TextInput(attrs={"class":"form-control","required":True, "placeholder":"Enter password"}),
    'name': forms.TextInput(attrs={"class":"form-control","required":True, "placeholder":"Name",}),
    
    'first_name': forms.TextInput(attrs={"class":"form-control","required":True, "placeholder":"Enter First Name",}),
    'last_name': forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter Last Name"}),
    
    'username': forms.TextInput(attrs={"class":"form-control","required":True, "placeholder":"Enter Username"}),
    'email': forms.EmailInput(attrs={"class":"form-control", "placeholder":"Enter Email"}),
    
    'password': forms.TextInput(attrs={"class":"form-control","required":True}),
    'old_password': forms.TextInput(attrs={"class":"form-control","required":True}),
    'password1': forms.TextInput(attrs={"class":"form-control","required":True}),
    'password2': forms.TextInput(attrs={"class":"form-control","required":True}),
    
    'is_active': forms.CheckboxInput(attrs={"class":"inline-success"}),
    'is_superuser' : forms.CheckboxInput(attrs={"class":"inline-success "}),
    'groups':forms.SelectMultiple(attrs={'class': 'multi-select'}),
    
    'profile_image': forms.ClearableFileInput(attrs={"class":"form-control dropzone", "placeholder":"Enter Username"}),
    'cover_image': forms.ClearableFileInput(attrs={"class":"form-control dropzone","placeholder":"Enter Username"}),
    
    'gender': forms.Select(attrs={"class":"form-control","required":True}),
    'birth_date':forms.DateInput(attrs={"class":"form-control", "placeholder":"Enter birth_date", "type":"date"}),
    'bio': forms.Textarea(attrs={"class":"form-control ", "rows":5, "placeholder":"bio body"}),
    'about': forms.Textarea(attrs={"class":"form-control summernoteEditor", "placeholder":"about body"}),

    'street': forms.TextInput(attrs={"class":"form-control","placeholder":"Enter First Name",}),
    'city': forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter Last Name"}),
    'state': forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter Last Name"}),

}