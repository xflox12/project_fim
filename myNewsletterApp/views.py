from django.shortcuts import render

from .models import NewsletterUser
from .forms import NewsletterUserSignUpForm

def newsletter_signup(request):
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            print("Sorry! This email already exists")  # users don't see this
        else:
            instance.save()

    context = {
        'form': form,
    }
    template = "newsletters_sign_up.html"
    return render (request, template, context)


def newsletter_unsubscribe(request):
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            NewsletterUser.objects.filter(email=instance.email).delete()  # if the email is found in our database, it will be deleted
        else:
            print("Sorry, but we did not find your email address")

    context = {
        "form": form,
    }

    template = "newsletters_unsubscribe.html"
    return render(request, template, context)