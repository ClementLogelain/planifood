from unicodedata import name
from django.urls import path
from . import views
from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [

    path('users/', views.getUsers, name="users"),
    path('usersFull/', views.getUsersFull, name="users_full"),
    path('auth/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('ingredients/', views.ingredientsLP, name="ingredients"),
    path('ingredients/<str:id>/', views.ingredientsUDG, name="ingredient"),

    path('mealUsing/', views.mealUsingLP,  name='ingredients_used'),
    path('mealUsing/<str:id>/', views.mealUsingUDG, name='ingredient_used'),

    path('categories/', views.categoryLP, name="categories"),
    path('categories/<str:id>/', views.categoryUDG, name="category")
]
