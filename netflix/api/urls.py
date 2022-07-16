
from django.urls import path
from .views import about, index
urlpatterns = [
    path('index/', index),
     path('about/', about),
    
]
