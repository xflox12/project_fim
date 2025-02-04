from django import forms
from crispy_forms.helper import FormHelper

from .models import NewsletterUser


class NewsletterUserSignUpForm(forms.ModelForm):
    helper = FormHelper() # from Crispy Forms library
    helper.form_show_labels = False

    class Meta:
        model = NewsletterUser
        fields = ['email']

        def clean_email(self): # it normalises the data before sending it to the view
            email = self.cleaned_data.get('email')

            return email

