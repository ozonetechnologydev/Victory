from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm, AdminPasswordChangeForm


from accounts.models import Address, User
from main.formWidget import WIDGETS
#===========================================================================




#===========================================================================
class HtmxUserCreationForm(forms.ModelForm):
    password = models.CharField(max_length=20)
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password']
        widgets = {
            'first_name': forms.TextInput(attrs={"class":"form-control","required":True, "placeholder":"Enter First Name",}),
            'last_name': forms.TextInput(attrs={"class":"form-control", "required":True, "placeholder":"Enter Last Name"}),
            'email': forms.EmailInput(attrs={"class":"form-control" ,"required":True, "placeholder":"Enter Email"}),
            'password': forms.TextInput(attrs={"class":"form-control","type":"password","required":True, "placeholder":"Enter Password"}),
        }
#===========================================================================



#===========================================================================
class HtmxUserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']
        widgets = {
            'first_name': forms.TextInput(attrs={"class":"form-control","required":True, "placeholder":"Enter First Name",}),
            'last_name': forms.TextInput(attrs={"class":"form-control", "required":True, "placeholder":"Enter Last Name"}),
            'email': forms.EmailInput(attrs={"class":"form-control" ,"required":True, "placeholder":"Enter Email"}),
        }
#===========================================================================



#===========================================================================
class AuthenticForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['email','password']
        widgets = {
            'email': forms.EmailInput(attrs={"class":"form-control" ,"required":True, "placeholder":"Enter Email"}),
            'password': forms.TextInput(attrs={"class":"form-control","type":"password","required":True, "placeholder":"Enter Password"}),
        }
#===========================================================================

#===========================================================================
class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        # exclude = ['password','date_joined','date_joined','is_staff','last_login','user_permissions']
        fields = ['first_name','last_name','username','email','user_permissions','groups', 'is_active','is_superuser', 'groups',]
        widgets = {
            'first_name': forms.TextInput(attrs={"class":"form-control","required":True, "placeholder":"Enter First Name",}),
            'last_name': forms.TextInput(attrs={"class":"form-control", "required":True, "placeholder":"Enter Last Name"}),
            'username': forms.TextInput(attrs={"class":"form-control" ,"required":False, "placeholder":"Enter Username"}),
            'email': forms.EmailInput(attrs={"class":"form-control" ,"required":True, "placeholder":"Enter Email"}),
            'is_active': forms.CheckboxInput(attrs={"class":"inline-success"}),
            'is_superuser' : forms.CheckboxInput(attrs={"class":"inline-success "}),
            'groups':forms.SelectMultiple(attrs={'class': 'multi-select'}),
            'user_permissions':forms.SelectMultiple(attrs={'class': 'multi-select'}),
        }
#===========================================================================


#===========================================================================
class AdminPassChangeForm(AdminPasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password','password1']
        widgets = {
            'old_password': forms.TextInput(attrs={"class":"form-control","type":"password","required":True, "placeholder":"Enter Old Password"}),
            'password1': forms.TextInput(attrs={"class":"form-control","type":"password","required":True, "placeholder":"Enter Password 1"}),
            'password2': forms.TextInput(attrs={"class":"form-control","type":"password","required":True, "placeholder":"Enter Password 2"}),
        }
#===========================================================================


#===========================================================================
class PassChangeForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password','password1']
        widgets = {
            'old_password': forms.TextInput(attrs={"class":"form-control","type":"password","required":True, "placeholder":"Enter Old Password"}),
            'password1': forms.TextInput(attrs={"class":"form-control","type":"password","required":True, "placeholder":"Enter Password 1"}),
            'password2': forms.TextInput(attrs={"class":"form-control","type":"password","required":True, "placeholder":"Enter Password 2"}),
        }
#===========================================================================



#===========================================================================
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password1','password2']
        widgets = {
            'first_name': forms.TextInput(attrs={"class":"form-control","required":True, "placeholder":"Enter First Name",}),
            'last_name': forms.TextInput(attrs={"class":"form-control", "required":True, "placeholder":"Enter Last Name"}),
            'email': forms.EmailInput(attrs={"class":"form-control","required":True, "placeholder":"Enter Email"}),
            'password1': forms.TextInput(attrs={"class":"form-control","type":"password","required":True, "placeholder":"Enter Password 1"}),
            'password2': forms.TextInput(attrs={"class":"form-control","type":"password","required":True, "placeholder":"Enter Password 2"}),
        }
#===========================================================================


#===========================================================================
class updateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']
        widgets = {
            'first_name': forms.TextInput(attrs={"class":"form-control","required":True, "placeholder":"Enter First Name",}),
            'last_name': forms.TextInput(attrs={"class":"form-control", "required":True, "placeholder":"Enter Last Name"}),
            'username': forms.TextInput(attrs={"class":"form-control" ,"required":True, "placeholder":"Enter Username"}),
            'email': forms.EmailInput(attrs={"class":"form-control","required":True,  "placeholder":"Enter Email"}),
        }
#===========================================================================


#===========================================================================
class updateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['birth_date','about', 'bio', 'gender']
        widgets = {
            'gender': forms.Select(attrs={"class":"form-control","required":True, "placeholder":"Enter Gender",}),
            'birth_date':forms.DateInput(attrs={"class":"form-control", "placeholder":"Enter Birth Date", "type":"date"}),
            'bio': forms.Textarea(attrs={"class":"form-control ", "rows":5, "placeholder":"Bio Body"}),
            'about': forms.Textarea(attrs={"class":"form-control summernoteEditor", "placeholder":"About Body"}),
        }
#===========================================================================


#===========================================================================
class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street','city','state']
        widgets = {
            'street': forms.TextInput(attrs={"class":"form-control","placeholder":"Street",}),
            'city': forms.TextInput(attrs={"class":"form-control", "placeholder":"City"}),
            'state': forms.TextInput(attrs={"class":"form-control", "placeholder":"State"}),
        }
#===========================================================================


