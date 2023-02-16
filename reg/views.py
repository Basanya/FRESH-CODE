from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import createform
# Create your views here.
def register(request):
    form = createform()

    if request.method=="POST":
        form = createform(request.POST)
        if form.is_valid():
            form.save()
        name = form.cleaned_data.get("username")
        messages.success(request, f"Hey! {name}, your account was successfully created")
        return redirect("login")
    
    context = {'form':form}
    return render(request, 'reg/register.html', context)

def my_login(request):
    context = {}
    return render(request, 'reg/login.html', context)