from django.shortcuts import render, redirect
from myLoginApp.models import Profile
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


def profile_view_temp(httprequest, *args, **kwargs):  # view to
    profile = Profile.objects.get(UserId=httprequest.user.id)
    context = {
        "User": httprequest.user
    }
    if profile.Picture:
        context["Profile"] = profile
    return render(httprequest, "myprofile.html", context)


def profile_change_password(httprequest):
    if httprequest.method == "POST":
        form = PasswordChangeForm(httprequest.user, httprequest.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(httprequest, user)
            return redirect("/profile")

    context = {
        "form": PasswordChangeForm(httprequest.user)
    }
    return render(httprequest, "changePassword.html", context)

