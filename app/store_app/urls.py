from django.urls import path
from .views import index,product,cart

urlpatterns=[
    path('',index),
    path('product/',product),
    path('cart/',cart),
]