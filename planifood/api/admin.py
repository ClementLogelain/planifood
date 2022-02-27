from django.contrib import admin
from .models import Meal, MealUsing, Planification, Category, Ingredient

# Register your models here.

admin.site.register(Meal)
admin.site.register(Planification)
admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(MealUsing)