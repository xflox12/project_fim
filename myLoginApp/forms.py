from django import forms
from .models import User

class create_user_form(forms.Form): #form the people will see when registering for the first time
    class Meta: #defining the data
        model=User
        fields=["Firstname", "Surname", "Nickname", "Email", "Picture", "Owner" ] #inputs users will need to fill out while registering

