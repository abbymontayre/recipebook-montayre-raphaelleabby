from django import forms

from .models import Recipe, RecipeImage, RecipeIngredient


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["name"]


class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ["image", "description"]


class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ["name", "quantity"]
