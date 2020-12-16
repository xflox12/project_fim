from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import user_registration_form
from django.contrib.auth.models import User


def user_registration(httprequest):

    if httprequest.method == "POST":

        # ATTENTION: httprequest.FILES is necessary for uploading the picture of the user!!!
        form = user_registration_form(httprequest.POST, httprequest.FILES)
        print(form)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.Picture = form.cleaned_data.get('Picture')

            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(httprequest, user)

            context = {
                "username": form.cleaned_data.get('username')
            }

            return redirect('/home', context)
        else:
            return render(httprequest, "registration.html", {'form': form, 'register': True})

    else:
        form = user_registration_form()

    return render(httprequest, "registration.html", {'form': form, 'register': True})


def edit_user_profile(httprequest):
    """view to update the user profile information (except password)"""
    """the view is implemented in the myLoginApp because it refers back to the user registration form"""

    form = user_registration_form(instance=httprequest.user)

    if httprequest.method == "POST":
        form = user_registration_form(data=httprequest.POST, files=httprequest.FILES, instance=httprequest.user)
        print(form.is_valid())
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.Picture = form.cleaned_data.get('Picture')

            user.save()

            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(httprequest, user)
            return redirect("/profile")
        else:
            return render(httprequest, "registration.html", {'form': form, 'register': False})
    return render(httprequest, "registration.html", {'form': form, 'register': False})


def delete_user_profile(httprequest):
    """This function deletes an user-profil"""
    profile = User.objects.get(id=httprequest.user.id)
    if httprequest.POST:
        profile.delete()
    return redirect("/logout")




