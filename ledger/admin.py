from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Ingredient, Profile, Recipe, RecipeIngredient, RecipeImage


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    fields = ("ingredient", "quantity")


class RecipeImageInline(admin.TabularInline):
    model = RecipeImage
    fields = ("image", "description")


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    list_display = ("id", "name", "author_name")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    list_filter = ("created_on", "updated_on")
    inlines = [RecipeIngredientInline, RecipeImageInline]
    fieldsets = [
        (
            "Details",
            {
                "fields": [
                    ("name", "author"),
                ]
            },
        ),
    ]

    @admin.display(description="author")
    def author_name(self, obj):
        if obj.author_id and obj.author:
            return obj.author.name
        return "(No author)"


class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ("name", "user")
    search_fields = ("name", "user__username")


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    search_fields = ("name",)


class RecipeImageAdmin(admin.ModelAdmin):
    model = RecipeImage
    list_display = ("id", "recipe", "description")
    list_display_links = ("id", "description")
    search_fields = ("description", "recipe__name")


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeImage, RecipeImageAdmin)
