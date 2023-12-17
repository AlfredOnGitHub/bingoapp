from django.shortcuts import render, redirect
from . models import Juego
import random

def juego(request):
    juego_actual, creado = Juego.objects.get_or_create(id=1)

    if request.method == 'POST':
        if 'nuevo_numero' in request.POST:
            numero_nuevo = dar_numero(juego_actual.numeros_dichos)
            juego_actual.numeros_dichos.append(numero_nuevo)
            juego_actual.save()
        
        elif 'reiniciar' in request.POST:
            juego_actual.numeros_dichos.clear()
            juego_actual.save()
            return redirect('bingo_app:juego')
        
    context = {
        'numeros_dichos': juego_actual.numeros_dichos,
    }

    return render(request, 'bingo_app/juego.html', context)

def dar_numero(numeros_dichos):
    numero_nuevo = random.randint(1, 90)
    while numero_nuevo in numeros_dichos:
        numero_nuevo = random.randint(1, 90)
    return numero_nuevo

