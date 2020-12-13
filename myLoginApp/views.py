from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import user_registration_form


def edit_user_profile(httprequest):
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





