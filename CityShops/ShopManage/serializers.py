from rest_framework import serializers
from .models import *


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class StreetSerializer(serializers.ModelSerializer):

    city = CitySerializer(read_only=True, many=False)

    class Meta:
        model = Street
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Street
        fields = '__all__'


