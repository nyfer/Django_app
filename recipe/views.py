# Create your views here.
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from .forms import RecipeForm, IngredientForm, PreparationStepForm
from .models import Recipe, Ingredient, PreparationStep

def index(request):
    return render(request, 'index.html', {
        'recipes': Recipe.objects.filter(),
    })
    

def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            return HttpResponseRedirect(reverse('recipe:create_ingredients', kwargs={'recipe_id': recipe.pk}))
        else:
            messages.error(request, "Please input the required data")
                
    return render(request, 'create_recipe.html', {
        'form': RecipeForm()
    })
    
def create_ingredients(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            messages.error(request, "Please input the required data")
                
    return render(request, 'create_ingredient.html', {
        'form': IngredientForm(initial={'recipe':recipe.id}),
        'ingredients': Ingredient.objects.filter(recipe=recipe),
        'recipe': recipe,
    })
    
    
def create_steps(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == 'POST':
        form = PreparationStepForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            messages.error(request, "Please input the required data")
                
    return render(request, 'create_steps.html', {
        'form': PreparationStepForm(initial={'recipe':recipe.id}),
        'steps': PreparationStep.objects.filter(recipe=recipe),
        'recipe': recipe,
    })
    
    
def view_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)               
    return render(request, 'view_recipe.html', {
        'recipe': recipe,
        'ingredients': Ingredient.objects.filter(recipe=recipe),
        'steps': PreparationStep.objects.filter(recipe=recipe),
    })
