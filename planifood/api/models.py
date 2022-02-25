from email.policy import default
from django.db import models
from enum import Enum
from django.contrib.auth.models import User

# Create your models here.

class Mesure(Enum):
    ML = 1
    MG = 2
    CL = 3
    CG = 4
    G = 5
    L = 6
    KG = 7


class Meal(models.Model):
    title = models.CharField(max_length=45, unique=True)
    process = models.TextField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    isBasic = models.BooleanField(default=True, blank=True)
    owner = models.ForeignKey(User, related_name='meals', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.title


class Planification(models.Model):
    panified_at = models.DateTimeField(null=True,  blank=True)
    owner = models.ForeignKey(User, related_name='planifications', on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, related_name='planned', on_delete=models.CASCADE)

    def __str__(self):
        return self.panified_at," - ", self.meal


class Category(models.Model):
    name = models.CharField(max_length=60 ,unique=True, null=True, blank=True)
    
    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=60, unique=True, null=True, blank=True)
    category = models.ForeignKey(Category, related_name='ingredients', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class IngredientUsed(models.Model):
    quantity = models.IntegerField(default=0, null=True)
    mesure = Mesure(value=Mesure.KG)
    using = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(User, related_name='ingredients', on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, related_name='usings', on_delete=models.CASCADE)

    def __str__(self):
        return self.ingredient
