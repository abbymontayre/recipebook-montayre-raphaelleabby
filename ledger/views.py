
from django.shortcuts import render
from .models import *

def recipe_list(request):
    recipes = Recipe.objects.all()
    context = {
        "recipes": recipes
        }

    return render(request, "recipes/recipe_list.html", context)

def recipe(request, name):
    recipe = Recipe.objects.get(name=name)
    ingredients = recipe.ingredients.all()
    context = {'name': str(recipe), 'ingredients': ingredients}
    return render(request, "./recipes/recipe.html", context)