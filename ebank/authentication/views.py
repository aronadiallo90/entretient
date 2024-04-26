from django.views.generic import View
from django.conf import settings
from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import authenticate, login, logout




def signup_page(request):  
    form = forms.SignupForm()
    if request.method == 'POST' :
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()       
            login(request,user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/signup.html', context = {'form' : form})
def logout_user(request):
    logout(request)
    return redirect('login')


