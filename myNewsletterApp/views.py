from django.contrib import messages
from django.shortcuts import render

from .models import NewsletterUser
from .forms import NewsletterUserSignUpForm

def newsletter_signup(request):
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            messages.warning(request, "Your email already exists in our database, please use another email", "alert alert-warning alert-dismissible")
        else:
            instance.save()
            messages.success(request, "Your email has been submitted to our database", "alert alert-success alert-dismissal")

    context = {
        'form': form,
    }
    template = "Newsletters/newsletters_sign_up.html"
    return render (request, template, context)


def newsletter_unsubscribe(request):
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            NewsletterUser.objects.filter(email=instance.email).delete()  # if the email is found in our database, it will be deleted
            messages.success(request, "Your email has been removed", "alert alert-success alert-dismissible")
        else:
            messages.warning(request, "Your email is not in our database", "alert alert-warning alert-dismissible")

    context = {
        "form": form,
    }

    template = "Newsletters/newsletters_unsubscribe.html"
    return render(request, template, context)