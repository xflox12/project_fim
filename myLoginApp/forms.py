from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class user_registration_form(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address')
    Picture = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'Picture')



# class create_user_form(forms.ModelForm):  # form the people will see when registering for the first time
#    Password = forms.CharField(widget=forms.PasswordInput)

#    class Meta:  # defining the data
#        model = User
#        fields = ["Firstname", "Surname", "Nickname", "Email", "Password"]
#        # inputs users will need to fill out while registering
