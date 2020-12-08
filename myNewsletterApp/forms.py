from django import forms

from .models import NewsletterUser


class NewsletterUserSignUpForm(forms.ModelForm):
    class Meta:
        model = NewsletterUser
        fields = ['email']

        def clean_email(self): # it normalises the data before sending it to the view
            email = self.cleaned_data.get('email')

            return email

