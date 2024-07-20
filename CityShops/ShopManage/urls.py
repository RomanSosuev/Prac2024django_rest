from django.urls import path, include

from .views import GetListAllCities, GetListAllStreet, PostShop

urlpatterns = [
    path('', GetListAllCities.as_view()),
    path('street/', GetListAllStreet.as_view()),
    path('shop/', PostShop.as_view()),
]
