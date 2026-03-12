
from django.shortcuts import *
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *


def recipe_list(request):
    recipes = Recipe.objects.all()
    context = {
        "recipes": recipes
    }

    return render(request, "recipes/recipe_list.html", context)


@login_required
def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients = recipe.ingredients.all()
    images = recipe.image.all()
    context = {
        'recipe_id': recipe.pk,
        'name': str(recipe),
        'author': recipe.author.name,
        'ingredients': ingredients,
        'images': images
    }
    return render(request, "recipes/recipe.html", context)


@login_required
def recipe_add(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == "POST":
        form = RecipeForm(request.POST)
        ingredient_form = RecipeIngredientForm(
            request.POST, prefix="ingredient")

        if form.is_valid() and ingredient_form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = profile
            recipe.save()

            recipe_ingredient = ingredient_form.save(commit=False)
            ingredient, _ = Ingredient.objects.get_or_create(
                name=recipe_ingredient.name
            )
            recipe_ingredient.recipe = recipe
            recipe_ingredient.ingredient = ingredient
            recipe_ingredient.name = ingredient.name
            recipe_ingredient.save()

            return redirect(recipe.get_absolute_url())
    else:
        form = RecipeForm()
        ingredient_form = RecipeIngredientForm(prefix="ingredient")

    context = {
        "form": form,
        "ingredient_form": ingredient_form,
    }
    return render(request, "./recipes/recipe_add.html", context)


@login_required
def recipe_add_image(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    if request.method == "POST":
        form = RecipeImageForm(request.POST, request.FILES)

        if form.is_valid():
            recipe_image = form.save(commit=False)
            recipe_image.recipe = recipe
            recipe_image.save()

            return redirect(recipe.get_absolute_url())
    else:
        form = RecipeImageForm()

    context = {"form": form, "recipe": recipe}
    return render(request, "./recipes/recipe_add_image.html", context)
