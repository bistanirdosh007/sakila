from rest_framework import serializers
from .models import (
    Actor, Address, Category, City, Country, Customer, Film, FilmActor, 
    FilmCategory, Inventory, Language, Payment, Rental, Staff, Store
)


# Actor Serializer
class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


# Address Serializer
class AddressSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField()

    class Meta:
        model = Address
        fields = '__all__'


# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


# City Serializer
class CitySerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField()

    class Meta:
        model = City
        fields = '__all__'


# Country Serializer
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


# Customer Serializer
class CustomerSerializer(serializers.ModelSerializer):
    store = serializers.StringRelatedField()
    address = serializers.StringRelatedField()

    class Meta:
        model = Customer
        fields = '__all__'


# Film Serializer
class FilmSerializer(serializers.ModelSerializer):
    language = serializers.StringRelatedField()

    class Meta:
        model = Film
        fields = '__all__'


# FilmActor Serializer
class FilmActorSerializer(serializers.ModelSerializer):
    actor = serializers.StringRelatedField()
    film = serializers.StringRelatedField()

    class Meta:
        model = FilmActor
        fields = '__all__'


# FilmCategory Serializer
class FilmCategorySerializer(serializers.ModelSerializer):
    film = serializers.StringRelatedField()
    category = serializers.StringRelatedField()

    class Meta:
        model = FilmCategory
        fields = '__all__'


# Inventory Serializer
class InventorySerializer(serializers.ModelSerializer):
    film = serializers.StringRelatedField()
    store = serializers.StringRelatedField()

    class Meta:
        model = Inventory
        fields = '__all__'


# Language Serializer
class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


# Payment Serializer
class PaymentSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField()
    staff = serializers.StringRelatedField()
    rental = serializers.StringRelatedField()

    class Meta:
        model = Payment
        fields = '__all__'


# Rental Serializer
class RentalSerializer(serializers.ModelSerializer):
    inventory = serializers.StringRelatedField()
    customer = serializers.StringRelatedField()
    staff = serializers.StringRelatedField()

    class Meta:
        model = Rental
        fields = '__all__'


# Staff Serializer
class StaffSerializer(serializers.ModelSerializer):
    address = serializers.StringRelatedField()
    store = serializers.StringRelatedField()

    class Meta:
        model = Staff
        fields = '__all__'


# Store Serializer
class StoreSerializer(serializers.ModelSerializer):
    manager_staff = serializers.StringRelatedField()
    address = serializers.StringRelatedField()

    class Meta:
        model = Store
        fields = '__all__'
