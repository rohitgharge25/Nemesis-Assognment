from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail

from .forms import SignUpForm
from .models import database


def Sign_Up(request):
    if request.method == 'POST':
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            un = fm.cleaned_data['user_name']
            fn = fm.cleaned_data['first_name']
            ln = fm.cleaned_data['last_name']
            em = fm.cleaned_data['Email']
            pas = fm.cleaned_data['password']
            reg = database(user_name=un, first_name=fn, last_name=ln, Email=em, password=pas)
            reg.save()
            fm=SignUpForm()

    else:
        fm=SignUpForm()

    return render(request,'app1/signup.html',{'form':fm})


def user_login(request):
   if request.method == "POST":
      fm=AuthenticationForm(request=request,data=request.POST)
      if fm.is_valid():

         uname = fm.cleaned_data['user_name']
         upass = fm.cleaned_data['password']
         database = authenticate(user_name=uname,password=upass)
         if database is not None:
            login(request,database)
      return redirect('profile')

   else:
      fm=AuthenticationForm()
   return render(request,'app1/userlogin.html',{'form':fm})



def user_profile(request):
   fm=database.objects.all()
   return render(request,'app1/profile.html',{'f':fm})

def delete(request,id):
    if request.method=="POST":
        pi=database.objects.get(pk=id)
        pi.delete()
        return redirect('profile')


def update(request,id):
    if request.method=='POST':
        pi=database.objects.get(pk=id)
        fm=SignUpForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=database.objects.get(pk=id)
        fm=SignUpForm(instance=pi)


    return render(request,'app1/update.html',{'form':fm})

def back(request):
    return redirect('profile')

def logout(request):
    return redirect('/')


