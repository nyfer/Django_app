from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    fname = models.CharField(max_length=30, verbose_name="First Name")
    lname = models.CharField(max_length=30, verbose_name="Last Name")
    created = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.title
        
class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe)
    name = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.name
    
class PreparationStep(models.Model):
    recipe = models.ForeignKey(Recipe)
    step = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.step
