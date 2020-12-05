from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest


# Create your views here.


def user_registration(httprequest):
    if httprequest.method == "POST":
        form = UserCreationForm(httprequest.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password1']
            user = authenticate(username=username, password=raw_password)
            login(httprequest, user)
#            context = {
#                "somestuff": "allOK"
#            }
            return redirect('/home')  # redirect page needs to be added

    else:
        form = UserCreationForm()
#       context = {
#           "form": form
#           }

    return render(httprequest, "registration.html", {'form': form})

#    return render(httprequest, "registration.html")



