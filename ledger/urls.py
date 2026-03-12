from django.urls import path
from .views import *

urlpatterns = [
    path('recipes/list/', recipe_list, name='recipe_list'),
    path('recipe/<int:pk>/', recipe_detail, name='recipe'),
    path('recipe/add/', recipe_add, name='recipe-add'),
    path('recipe/<int:pk>/add_image/', recipe_add_image, name='recipe-add-image'),
]

app_name = "ledger"
