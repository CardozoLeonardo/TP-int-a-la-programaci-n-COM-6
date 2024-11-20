# capa de vista/presentación

from django.shortcuts import redirect, render
from .layers.services import services
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
#Importamos requests y json para extraer la información del link y trabajar con ella
import requests
import json

def index_page(request):
    return render(request, 'index.html')

# Home: Lista de imagenes y favoritos
def home(request):
    #Lista para guardar las imagenes de todos los personajes
    images = [] 
    
    #Variable para guardar el link con la información de todos los personajes
    link=("https://rickandmortyapi.com/api/character")

    #Obtiene la información de los personajes
    contenido_link=requests.get(link)

    # Hace manipulable la información de los personajes
    data=json.loads(contenido_link.content)

    #Recorre la información de todos los personajes
    for element in data:
        images.append(element["images"])#Guarda la imagen de todos los personajes en la lista "images"

    # Lista de favoritos (vacía por ahora)
    favourite_list = []

    return render(request, 'home.html', {"images": images, "favourite_list": favourite_list})

# Buscar personajes (pendiente de implementación)
def search(request):
    search_msg = request.POST.get('query', '')

    if search_msg != '':
        # Implementar la lógica de búsqueda
        pass
    else:
        return redirect('home')

# Favoritos (funcionalidades relacionadas con el usuario logueado)
@login_required
def getAllFavouritesByUser(request):
    favourite_list = []
    return render(request, 'favourites.html', {"favourite_list": favourite_list})

@login_required
def saveFavourite(request):
    pass

@login_required
def deleteFavourite(request):
    pass

@login_required
def exit(request):
    pass
