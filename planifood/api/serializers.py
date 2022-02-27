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
        fields = ('id','title','process','duration','isBasic','owner')


class PlanificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planification
        fields = ('id','panified_at','owner','meal')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name')


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id','name','category')

class MealUsingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealUsing
        fields = '__all__'
