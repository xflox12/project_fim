from django.contrib import messages
from django.shortcuts import render

from .models import NewsletterUser
from .forms import NewsletterUserSignUpForm

def newsletter_signup(request):
    """ This function signs the user up to receive the community
    newsletter. The user is signed up using his/her email."""
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists(): # checks if the email provided already exists in our database
            messages.warning(request, "Your email already exists in our database, please use another email")
        else:
            instance.save()
            messages.success(request, "Your email has been submitted to our database")

    context = {
        'form': form,
    }
    template = "newsletters_sign_up.html"
    return render (request, template, context)


def newsletter_unsubscribe(request):
    """This function unsubscribes the user of receiving the newsletter.
    Thus, it deletes the user's email from our database."""
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            NewsletterUser.objects.filter(email=instance.email).delete()  # if the email is found in our database, it will be deleted
            messages.success(request, "Your email has been removed")
        else:
            messages.warning(request, "Your email is not in our database")

    context = {
        "form": form,
    }

    template = "newsletters_unsubscribe.html"
    return render(request, template, context)