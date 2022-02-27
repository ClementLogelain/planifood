from cgitb import reset
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from api.serializers import CategorySerializer, UserSerializer
from .models import Category, Ingredient, MealUsing, User

from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import IngredientSerializer, MealUsingSerializer, MyTokenObtainPairSerializer, UserFullSerializer

# ---------------------- USERS -------------------------


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUsersFull(request):
    users = User.objects.all()
    serializer = UserFullSerializer(users, many=True)
    return Response(serializer.data)


# -------------------- INGREDIENTS ---------------------


@api_view(['GET', 'POST'])
def ingredientsLP(request):
    if request.method == 'GET':
        ingredients = Ingredient.objects.all()
        serialzer = IngredientSerializer(ingredients, many=True)
        return Response(serialzer.data)

    elif request.method == 'POST':
        serializer = IngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def ingredientsUDG(request, id):
    if request.method == 'GET':
        ingredient = Ingredient.objects.get(id=id)
        serializer = IngredientSerializer(ingredient, many=False)
        if(not ingredient):
            return Response('wrong data!')
        return Response(serializer.data)

    elif request.method == 'PUT':
        ingredient = Ingredient.objects.get(id=id)
        serializer = IngredientSerializer(instance=ingredient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method  == 'DELETE':
        ingredient = Ingredient.objects.get(id=id)
        ingredient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# --------------------- MEAL USING ------------------------


@api_view(['GET', 'POST'])
def mealUsingLP(request):
    if request.method == 'GET':
        using = MealUsing.objects.all()
        serialzer = MealUsingSerializer(using, many=True)
        return Response(serialzer.data)

    elif request.method == 'POST':
        serializer = MealUsingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def mealUsingUDG(request, id):
    if request.method == 'GET':
        using = MealUsing.objects.get(id=id)
        serializer = MealUsingSerializer(using, many=False)
        if(not using):
            return Response('wrong data!')
        return Response(serializer.data)

    elif request.method == 'PUT':
        using = MealUsing.objects.get(id=id)
        serializer = MealUsingSerializer(instance=using, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method  == 'DELETE':
        using = MealUsing.objects.get(id=id)
        using.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# --------------------- CATEGORIES ---------------------------


@api_view(['GET', 'POST'])
def categoryLP(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serialzer = CategorySerializer(categories, many=True)
        return Response(serialzer.data)

    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def categoryUDG(request, id):
    if request.method == 'GET':
        category = Category.objects.get(id=id)
        serializer = CategorySerializer(category, many=False)
        if(not category):
            return Response('wrong data!')
        return Response(serializer.data)

    elif request.method == 'PUT':
        category = Category.objects.get(id=id)
        serializer = CategorySerializer(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method  == 'DELETE':
        category = Category.objects.get(id=id)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)