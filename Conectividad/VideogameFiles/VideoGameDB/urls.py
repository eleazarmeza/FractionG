from django.urls import path
from .views import PlayerView
from .views import CrearUsuario
from .views import InicioSesion
from .views import GuardarProgreso
from .views import VerProgreso
from .views import Scoreboard


urlpatterns= [
    path('players/', PlayerView.as_view(), name="player_list"),
    path('CrearUsuario/',CrearUsuario.as_view()),
    path('InicioSesion/',InicioSesion.as_view()),
    path('GuardarProgreso/',GuardarProgreso.as_view()),
    path('VerProgreso/',VerProgreso.as_view()),
    path('Scoreboard/',Scoreboard.as_view())
]