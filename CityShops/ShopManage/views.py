from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import City, Street
from .serializers import CitySerializer, StreetSerializer, ShopSerializer


class GetListAllCities(generics.ListAPIView):
    serializer_class = CitySerializer

    def get_queryset(self):
        return City.objects.all()


class GetListAllStreet(generics.ListAPIView):
    serializer_class = StreetSerializer

    def get_queryset(self):
        return Street.objects.all()


class PostShop(APIView):

    def post(self, request, format = None):
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)