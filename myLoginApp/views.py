from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import User
from .forms import create_user_form


# Create your views here.


def user_registration(httprequest, *args, **kwargs): # define the function for the registration form
    """this function consists of the creation of a user registration form and, after the user is successfully registered, it automatically logs him/her into their profile"""
    if httprequest.method == "POST":
        form = create_user_form(httprequest.POST)

        if form.is_valid():
            form.save()
            Nickname = form.cleaned_data['Nickname']
            Password = form.cleaned_data['Password']
            user = authenticate(Nickname=Nickname, Password=Password)
            login(httprequest, user)
            return redirect("") #redirect page needs to be added

    else:
        form = create_user_form()
        context = {
            "form": form
        }

    return render(httprequest, "registration.html", context)

