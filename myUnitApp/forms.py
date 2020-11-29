from django import forms
from .models import Unit


class UnitForm(forms.ModelForm):

    class Meta:  # defining the data
        model = Unit
        fields = ["Name", "Abbreviation"]

