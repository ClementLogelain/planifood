from dataclasses import field
from rest_framework import serializers
from .models import Category, Meal, MealUsing, Planification, Ingredient
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.forms.models import model_to_dict

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        # ...

        return token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email')

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'


class PlanificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planification
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class MealUsingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealUsing
        fields = '__all__'

class UserFullSerializer(serializers.ModelSerializer):
    ingredients_created=IngredientSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = ('id','username','email','ingredients_created')
