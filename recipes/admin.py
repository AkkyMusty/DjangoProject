from django.contrib import admin
from django.contrib.auth import get_user, get_user_model

# Register your models here.
from .models import Recipe, RecipeIngredient

# admin.site.register(RecipeIngredient)

User = get_user_model()

class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredient
    extra = 0
    # fields =['name', 'quantity', 'unit', 'direction']

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    list_display = ['name', 'user']
    readonly_fields = ['timestamp', 'updated']
    raw_id_fields = ['user']

admin.site.register(Recipe,RecipeAdmin)




