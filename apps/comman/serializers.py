from rest_framework import serializers
from .models import User,Country,City,State

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id','country_name']

class StateSerializer(serializers.ModelSerializer):
    state_country=CountrySerializer()
    class Meta:
        model = State
        fields = ['id','state_country', 'state_name']

class CitySerializer(serializers.ModelSerializer):
    city_country=CountrySerializer()
    city_state=StateSerializer()
    class Meta:
        model = City
        fields = ['id','city_name','city_country','city_state']

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'user_country','user_state','user_city']

class UserListSerializer(serializers.ModelSerializer):
    user_country=CountrySerializer()
    user_state=StateSerializer()
    user_city=CitySerializer()
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'user_country','user_state','user_city']
