from django import forms
from .models import Recipe

class create_recipe_form(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ("RecipeName", "Picture", "UserID", "Energy", "UnitID", "NumberPeople")
