from django import forms
from .models import Recipe, RecipeSteps, Ingredient

class create_recipe_form(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["RecipeName", "Picture", "Energy", "NumberPeople"] #errors obtained with UserID

class create_recipe_form2(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ["Quantity"] #errors obtained with IngredientID and FoodItemID

class create_recipe_form3(forms.ModelForm):
    class Meta:
        model = RecipeSteps
        fields = ["Duration", "StepNo", "Description", "Tips"]

