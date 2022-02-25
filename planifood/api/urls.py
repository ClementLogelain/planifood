from unicodedata import name
from django.urls import path
from . import views
from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [

    path('users/', views.getUsers, name="users"),
    path('auth/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('ingredients/', views.getIngredients, name="ingredients"),
    path('ingredients/post/', views.postIngredient, name="post"),

    path('categories/', views.getCategories, name="categories"),
    path('categories/<str:id>/', views.getCategory, name="category")
]
