#===========================================================================
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth import update_session_auth_hash, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from django.core.mail import send_mail

from accounts.models import User
from students.models import Student
from teachers.models import Teacher
from main.decorators import admin_only, allowed_users, unauthenticated
from accounts.forms import (AuthenticForm, PassChangeForm,AdminPassChangeForm, RegisterForm,  updateUserForm,)
#===========================================================================


#===========================================================================
@unauthenticated
def user_login(request):
	form = AuthenticForm()
	if request.method == "POST":
		form = AuthenticForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('home')
	return render(request, 'accounts/public/authentication_signin.html', context={"form": form})
#===========================================================================
#===========================================================================
def user_logout(request):
    logout(request)
    return redirect('home')
#===========================================================================
#===========================================================================
@unauthenticated
def user_register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            
            user = authenticate(email=email, password=password)
            user.email_user(
                  'Welcome to victory wisdom school',
                  '''For Disney’s “Cars”, animated racing automobiles inspire 
                  children and although this may lead to children running around like 
                  they’re on the track, this can be used to a teachers advantage. 
                  Displaying classroom rules with signage at the front of the room
                  and using acronyms:\n R - Respect - everyone in the school, yourself, 
                  your peers and the school property.\n A - Attitude - have a positive one, 
                  treat others with kindness and work hard.\n C - Cooperate - work together
                  with one another and always try your best.\n E - Excellence - use this as
                  the key to succeed.''',
                  fail_silently=True,
              )
            if user is not None:
                login(request, user)
                return redirect('home')
            return redirect('login')

    context = {'form': form,}
    return render(request, 'accounts/public/authentication_signup.html', context)
#===========================================================================



#===========================================================================
@admin_only
@login_required(login_url='login')
def create_user(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("user_details", user.id)

    context = {'form': form,}
    return render(request, 'users/admin/create_user.html', context)
#===========================================================================

#===========================================================================
@login_required(login_url='login')
def update_user_account(request):
  form = updateUserForm(instance = request.user)
  context = {
    "form":form,
    "show_messages":True,
    "title":"Edit Address",
    "action":reverse("update_user_account"),
  } 
  if request.method == 'POST':
    form = updateUserForm(request.POST, instance = request.user)
    print(form.errors)
    if form.is_valid():
      form.save()
      messages.success(request, 'Accounts is Updated successfully.')
      context = {
        **context,
        "form":form,
        "alert":{"title":"Success","body":"Accounts is Updated successfully","type":"success",},
      }
  return render(request, "components/forms.html", context)
#===========================================================================


#===========================================================================
@login_required(login_url='login')
def close_user_account(request):
  user = User.objects.get(id=request.user.id)
  logout(request)
  user.is_active = False
  user.save()
  return redirect("home")
#===========================================================================

#===========================================================================
@login_required(login_url='login')
def delete_user_account(request):
  user = User.objects.get(id=request.user.id)
  logout(request)
  user.delete()
  return redirect("home")
#===========================================================================



#===========================================================================
@admin_only
@login_required(login_url='login')
def delete_user(request, pk):
  user = User.objects.get(id=pk)
  user.delete()
  return redirect("users_list")
#===========================================================================
@admin_only
@login_required(login_url='login')
def multi_close_and_delete_user_account(request):
  
  users_id = request.POST.getlist("columns")
  users = User.objects.filter(id__in=users_id)
  action = request.POST.get("action")
  if users.exists() and not action in ["null", None, "None", [], '[]', [''], '']:
    for user in users:
      if action == "delete":
        user.delete()
        print("user is deleted")
        
      elif action == "activate":
        user.is_active = True
        user.save()
        print("user is deactivated")
        
      elif action == "deactivate":
        user.is_active = False
        user.save()
        print("user is deactivated")
        
  redirect_to = request.META.get("HTTP_REFERER")
  if not redirect_to in ["null", None, "None", [], '[]', [''], '']:
      redirect_to = "users_list"
  return redirect(redirect_to)

#===========================================================================
@admin_only
@login_required(login_url='login')
def admin_change_password(request):
    form = AdminPassChangeForm(user = request.user)
    print(request.POST)
    context = {
      "show_messages":True,
      "title":"Change Password",
      "action":reverse("admin_change_password"),
    } 
    if request.method == 'POST':
        form = AdminPassChangeForm(user=request.user, data=request.POST)
        print(form.errors)
        if form.is_valid():
          form.save()
          update_session_auth_hash(request, form.user)
          messages.success(request, 'Password is Changed successfully.')
          context = {
            **context,
            "alert":{"title":"Success","body":"Password is Changed successfully","type":"success",},
          }
          print(">>>>>>>>>>>>>>>>>>>>>>>>")
          
    context = {  **context,"form":form,  }
    return render(request, "components/forms.html", context)
#===========================================================================





#===========================================================================
@login_required(login_url='login')
def change_password(request):
    form = PassChangeForm(user = request.user)
    context = {
      "form":form,
      "show_messages":True,
      "title":"Change Password",
      "action":reverse("change_password"),
    } 
    if request.method == 'POST':
        form = PassChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password is Changed successfully.')
            context = {
              **context,
              "form":form,
              "alert":{"title":"Success","body":"Password is Changed successfully","type":"success",},
            }

    return render(request, "components/forms.html", context)
#===========================================================================