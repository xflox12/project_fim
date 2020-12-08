from django import forms
from .models import Recipe, RecipeSteps, Ingredient

class create_recipe_form(forms.ModelForm):
    #Userid = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Recipe
        fields = ["RecipeName", "Picture","Energy", "UnitId", "NumberPeople"]

class create_recipe_form2(forms.ModelForm):

    class Meta:
        model = Ingredient
        fields = ["IngredientId", "Quantity", "UnitId", "FoodItemId", "Note"]

class create_recipe_form3(forms.ModelForm):
    class Meta:
        model = RecipeSteps
        fields = ["Duration", "StepNo", "Description", "Tips"]