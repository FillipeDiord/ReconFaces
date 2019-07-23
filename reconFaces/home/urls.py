from django.urls import path
from .views import  home, meu_logout

urlpatterns = [
    path('', home, name='home'),
    path('logout/', meu_logout, name="logout"),
]


