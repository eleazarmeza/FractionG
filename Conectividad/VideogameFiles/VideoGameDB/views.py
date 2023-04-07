from django.shortcuts import render
from django.views import View
from .models import Player
from .models import Players
from django.http import JsonResponse
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
class PlayerView(View):
    def get(self, request):
        players = list(Player.objects.values())
        if len(players)>0:
            datos={
                "message":"Success",
                "players":players
            }
        else:
            datos = {
                "message":"No players found"
            }
        return JsonResponse(datos)
    def post(self, request):
        pass
    def put(self, request):
        pass
    def delete(self, request):
        pass


class CrearUsuario(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
    
    def get(self, request):
        players = Players.objects.all()
        #data = [{'Crear usuario:':'----'},{'Grupo':'Grupo 3'},{'Número de lista':'17'},{'Password':'*********'}]
        data = [
            {
                'players':list(players.values())
            }
        ]
        
        return JsonResponse(data, safe=False)
    
    def post(self,request):
        data = json.loads(request.body.decode('utf-8'))
        Grupo = data['Grupo']
        Numero_de_Lista = data['Numero_de_Lista']
        Password = data['Password']

        jugador_existente = Players.objects.filter(Grupo=Grupo, Numero_de_Lista=Numero_de_Lista).first()
        if jugador_existente:
            Usuario_existente = [{"El jugador":"ya existe"}]
            return JsonResponse(Usuario_existente, safe=False)
        else:
            jugador = Players()
            jugador.Grupo = data['Grupo']
            jugador.Numero_de_Lista = data['Numero_de_Lista']
            jugador.Password = data['Password']
            jugador.save()
            Usuario_Creado = [{"Usuario Creado":"----"}]
            return JsonResponse(Usuario_Creado, safe=False)


class InicioSesion(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
    def get(self, request):
        data = [{'Inicio de sesión:':'----'},{'Grupo':'Grupo 2'},{'Número de lista':'17'},{'Password':'*********'}]
        #return JsonResponse(data, safe=False)
        return HttpResponse(data)
    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        Grupo = data['Grupo']
        Numero_de_Lista = data['Numero_de_Lista']
        Password = data['Password']
        
        jugador_existente = Players.objects.filter(Grupo=Grupo, Numero_de_Lista=Numero_de_Lista).first()
        if jugador_existente:
            if jugador_existente.Password == Password:
                Usuario_existente = [{"Inicio de sesión exitoso": "----"}]
                return JsonResponse(Usuario_existente, safe=False)
            else:
                Usuario_Existente = [{"Usuario o contraseña incorrecta": "----"}]
                return JsonResponse(Usuario_Existente, safe=False)
        else:
            Usuario_Existente = [{"Usuario o contraseña incorrecta": "----"}]
            return JsonResponse(Usuario_Existente, safe=False)

class GuardarProgreso(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
    def get(self, request):
        return HttpResponse('Progreso Guardado')
    def post(self, request):
        data = json.loads(request.body)
        id = data["id"]
        Pregunta = data["Pregunta"]
        Respuesta_1 = data["Respuesta_1"]
        Respuesta_2 = data["Respuesta_2"]
        Respuesta_3 = data["Respuesta_3"]
        Respuesta_4 = data["Respuesta_4"]
        Respuesta_Correcta = ["Respuesta_Correcta"]
        Respuesta_del_Alumno = data["Respuesta_del_Alumno"]
        Tiempo = data["Tiempo"]
        Nivel = data["Nivel"]
        Time_Stamp = data["Time_Stamp"]
        Progreso = {"Progreso Guardado":"------"}
        return JsonResponse(Progreso)

class VerProgreso(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
    def get(self, request):
        data = {"Te quedaste en el nivel 8 ":"-----"}

        return JsonResponse(data)
    def post(self, request):
        pass

class Scoreboard(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
    def get(self, request):
        return HttpResponse('Scoreboard')
    def post(self, request):
        pass

        


