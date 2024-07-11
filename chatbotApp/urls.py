from django.urls import path
from .views import *

urlpatterns = [
    path('', SignUpPage,name='signup'),
    path('login/',LoginPage,name ='login'),
    path('logout/',LogOutPage,name = 'logout'),
    path('chatbot/',chatbot,name = 'chatbot'),
]