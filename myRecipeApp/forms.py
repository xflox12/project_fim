from django import forms
from .models import Recipe, RecipeSteps

class create_recipe_form(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["RecipeName", "Picture", "Energy", "NumberPeople"]

class create_recipe_form2(forms.ModelForm):
    class Meta:
        model = RecipeSteps
        fields = ["Duration", "StepNo", "Description", "Tips"]
