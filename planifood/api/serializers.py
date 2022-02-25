from rest_framework import serializers
from .models import Category, Meal, Planification, Ingredient, IngredientUsed
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
        fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id','name','category')

class IngredientUsedSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientUsed
        fields = ('id','quantity','mesure','using','owner','ingredient')
