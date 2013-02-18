'''
Created on Feb 17, 2013

@author: Noel
'''
from django.conf.urls import patterns,url


urlpatterns = patterns('recipe.views',
    
    url(r'^$', 'index', name='index'),
    url(r'^create/recipe/$', 'create_recipe', name='create_recipe'),
    url(r'^create/ingredients/(?P<recipe_id>\d+)/$', 'create_ingredients', 
        name="create_ingredients"),
    url(r'^create/steps/(?P<recipe_id>\d+)/$', 'create_steps', 
        name="create_steps"),
    url(r'^view/recipe/(?P<recipe_id>\d+)/$', 'view_recipe', 
        name="view_recipe"),
)