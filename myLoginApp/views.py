from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import user_registration_form
from django.http import HttpResponse, HttpRequest


# Create your views here.


def user_registration(httprequest):

    if httprequest.method == "POST":

        print ('XX1')

        # ATTENTION: httprequest.FILES is necessary for uploading the picture of the user!!!
        form = user_registration_form(httprequest.POST, httprequest.FILES)
        print ('XX2')
        print (form)
        print ('XX2a')
        if form.is_valid():
            print('XX3')
            user = form.save()
            user.refresh_from_db()
            print('XX4')
            user.profile.Picture = form.cleaned_data.get('Picture')

            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            print('XX5')
            login(httprequest, user)
#            context = {
#                "somestuff": "allOK"
#            }
            print('XX6')
            return redirect('/home')  # redirect page needs to be added

    else:
        form = user_registration_form()
#       context = {
#           "form": form
#           }

    return render(httprequest, "registration.html", {'form': form})

#    return render(httprequest, "registration.html")



