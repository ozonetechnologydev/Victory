from django.shortcuts import render, redirect



def create_raview(request, form):
    return render(request, "components/forms.html")
