from django.urls import path
from .consumers import  WSConsumer

ws_urlpatterns=[
    path('stream',WSConsumer.as_asgi()),
]