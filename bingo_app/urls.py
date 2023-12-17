from django.urls import path
from .views import juego

app_name = 'bingo_app'

urlpatterns = [
    path('', juego, name='juego'),
]