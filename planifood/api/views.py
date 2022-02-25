from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import api

from api.serializers import CategorySerializer, UserSerializer
from .models import Category, Ingredient, User

from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import IngredientSerializer, MyTokenObtainPairSerializer

# USERS

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

# INGREDIENTS
@api_view(['GET'])
def getIngredients(request):
    ingredients = Ingredient.objects.all()
    serializer = IngredientSerializer(ingredients, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def postIngredient(request, ingr):
    ingredient = Ingredient.objects.create(ingr)
    serializer = IngredientSerializer(ingr, manu=False)

    return Response(serializer.data)


# CATEGORIES

@api_view(['GET'])
def getCategories(request):
    categories = Category.objects.all()
    serialzer = CategorySerializer(categories, many=True)
    return Response(serialzer.data)

@api_view(['GET'])
def getCategory(request, id):
    category = Category.objects.get(id=id)
    serializer = CategorySerializer(category, many=False)
    if(not category):
        return Response('wrong data!')
    return Response(serializer.data)