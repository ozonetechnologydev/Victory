from multiprocessing import AuthenticationError
from django.shortcuts import render, redirect


def admin_only(views_func):
  def wrapper_func(request, *args, **kwarg):
    if request.user.is_superuser:
      return views_func(request, *args, **kwarg)
    else:
      return redirect("home")
  return wrapper_func

def unauthenticated(views_func):
  def wrapper_func(request, *args, **kwarg):
    if request.user.is_authenticated:
      return redirect("home")
    else:
      return views_func(request, *args, **kwarg)
  return wrapper_func

def allowed_users(permissions=[], require_all=False , redirect_to="login"):
  def decorator(views_func):
    def wrapper_func(request, *args, **kwarg):
      all_user_perms =  list(request.user.get_all_permissions())
      if require_all:
        has_num_parm = 0
        for perms in permissions:
          if perms in all_user_perms:
            has_num_parm += 1
        if has_num_parm == len(permissions):
          return views_func(request, *args, **kwarg)
        else:
          return redirect(redirect_to) 
      else:
        for perms in permissions:
          if perms in all_user_perms:
            return views_func(request, *args, **kwarg)
        else:
          return redirect(redirect_to)  #render(request, 'error/unauthorized_to_page.html')
      
    return wrapper_func
  return decorator
