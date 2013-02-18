'''
Created on Feb 18, 2013

@author: Noel
'''
from django.contrib import admin
from .models import Recipe, Ingredient, PreparationStep

class IngredientInline(admin.StackedInline):
    model = Ingredient
    extra = 0
    
class PreparationStepInline(admin.StackedInline):
    model = PreparationStep
    extra = 0
    
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'fname', 'lname', 'created')
    search_fields = ('title', 'fname', 'lname')
    inlines = [IngredientInline, PreparationStepInline]

admin.site.register(Recipe, RecipeAdmin)