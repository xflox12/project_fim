from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import user_registration_form
from django.http import HttpResponse, HttpRequest


# Create your views here.


def user_registration(httprequest):

    if httprequest.method == "POST":

        # ATTENTION: httprequest.FILES is necessary for uploading the picture of the user!!!
        form = user_registration_form(httprequest.POST, httprequest.FILES)

        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.Picture = form.cleaned_data.get('Picture')

            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(httprequest, user)
#            context = {
#                "somestuff": "allOK"
#            }
            return redirect('/home')  # redirect page needs to be added

    else:
        form = user_registration_form()
#       context = {
#           "form": form
#           }

    return render(httprequest, "registration.html", {'form': form})

#    return render(httprequest, "registration.html")



