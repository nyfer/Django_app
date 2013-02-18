'''
Created on Feb 17, 2013

@author: Noel
'''
from django.forms import ModelForm

from .models import Recipe, Ingredient, PreparationStep

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        
class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        
class PreparationStepForm(ModelForm):
    class Meta:
        model = PreparationStep
