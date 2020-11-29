from django import forms
from .models import User


class create_user_form(forms.ModelForm):  # form the people will see when registering for the first time
    Password = forms.CharField(widget=forms.PasswordInput)

    class Meta:  # defining the data
        model = User
        fields = ["Firstname", "Surname", "Nickname", "Email", "Password"]
        # inputs users will need to fill out while registering
