from django.urls import path

from myNewsletterApp.views import newsletter_signup, newsletter_unsubscribe

from .views import newsletter_signup, newsletter_unsubscribe

urlpatterns = [
    path('signupnewsletter/', newsletter_signup, name='newsletter_signup'),
    path('unsubscribenewsletter/', newsletter_unsubscribe, name='newsletter_unsubscribe'),
]