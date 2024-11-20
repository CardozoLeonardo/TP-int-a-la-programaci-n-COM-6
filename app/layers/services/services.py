# capa de servicio/lógica de negocio

from ..persistence import repositories
from ..utilities import translator
from ..transport import transport as lista_images

from django.contrib.auth import get_user

def getAllImages(input=None):
    # obtiene un listado de datos "crudos" desde la API, usando a transport.py.
    lista_images=getAllImages
    json_collection = [lista_images]

    # recorre cada dato crudo de la colección anterior, lo convierte en una Card y lo agrega a images.
    images = []

    for character in json_collection:
        card = {
        'id': character['id'],
        'name': character['name'],
        'image': character['image'],
        'status': character['status'],
    }
    images.append(card)

    return images

# añadir favoritos (usado desde el template 'home.html')
def saveFavourite(request):
    fav = {
    'id': request.POST.get('id'),
    'name':request.POST.get('name'),
    'image':request.POST.get('image'),
    'status':request.POST.get('status')
    }
    fav.user = request.user # le asignamos el usuario correspondiente.

    return repositories.saveFavourite(fav) # lo guardamos en la base.

# usados desde el template 'favourites.html'
def getAllFavourites(request):
    if not request.user.is_authenticated:
        return []
    else:
        user = get_user(request)

        favourite_list = [repositories.getFavouritesByUser(User)] # buscamos desde el repositories.py TODOS los favoritos del usuario (variable 'user').
        mapped_favourites = []

        for favourite in favourite_list:
            card = {
            'id':favourite.id,
            'name':favourite.name,
            'image':favourite.image,
            'status':favourite.status,
            } # transformamos cada favorito en una Card, y lo almacenamos en card.
            mapped_favourites.append(card)

        return mapped_favourites

def deleteFavourite(request):
    favId = request.POST.get('id')
    return repositories.deleteFavourite(favId) # borramos un favorito por su ID.