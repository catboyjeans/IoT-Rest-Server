from django.urls import path 

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('post/<slug:thing_name>',views.recieve_message),
    path('read/<slug:thing_name>',views.get_data),
]