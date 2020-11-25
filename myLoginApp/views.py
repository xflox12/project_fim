from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View, TemplateView   #import for class-based-view #import for template-view

from .forms import create_user_form
from django.contrib.auth import authenticate,login
# Create your views here.


def user_registration(httprequest, *args, **kwargs):  # define the function for the registration form
    if httprequest.method == "POST":
        form = create_user_form(httprequest.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['Email']  # username = email
            password = form.cleaned_data['Password']
            user = authenticate(Nickname=Nickname, Password=Password)
            login(httprequest, user)
            return redirect("")

    else:
        form = create_user_form()
        context = {
            "form": form
        }
    # return render(httprequest, "registration.html", context)
    return render(httprequest, "registration.html", context)


