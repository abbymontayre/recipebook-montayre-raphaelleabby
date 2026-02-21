
from django.shortcuts import *
from .models import *

def recipe_list(request):
    recipes = Recipe.objects.all()
    context = {
        "recipes": recipes
        }

    return render(request, "recipes/recipe_list.html", context)

def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients = recipe.ingredients.all()
    context = {'name': str(recipe), 'ingredients': ingredients}
    return render(request, "./recipes/recipe.html", context)