
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name= "home" ),
    path('login', login, name= "login" ),
    path('register', register, name= "register" ),
    path('apropos', apropos, name= "apropos" ),
    path('contact', contact, name= "contact" ),
    path('gallery', gallery, name= "gallery" ),
    
]