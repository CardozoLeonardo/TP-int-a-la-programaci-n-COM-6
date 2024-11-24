# capa de servicio/lógica de negocio

from ..persistence import repositories
from ..utilities import translator
from django.contrib.auth import get_user
from app.layers.transport import transport
from app.layers.utilities import card

transport.getAllImages()

def __hash__(x):
        return hash((x.url, x.name, x.status))

json_collection = [transport.getAllImages]

def getAllImages(input=None):
    # obtiene un listado de datos "crudos" desde la API, usando a transport.py.
    images = []
    for element in json_collection:
    # recorre cada dato crudo de la colección anterior, lo convierte en una Card y lo agrega a images
        images.append=_hash_(element)

    return images
images=getAllImages
repositories.saveFavourite(images)

# añadir favoritos (usado desde el template 'home.html')
def saveFavourite(request):
    fav = _hash_(request) # transformamos un request del template en una Card.
    fav.user = get_user(request) # le asignamos el usuario correspondiente.

    return repositories.saveFavourite(fav) # lo guardamos en la base.

# usados desde el template 'favourites.html'
def getAllFavourites(request):
    if not request.user.is_authenticated:
        valor1=("El usuario no está autenticado")
        return [valor1]
    else:
        user = get_user(request)

        repositories.getAllFavourites(user)

        favourite_list = [repositories.getAllFavourites(user)] # buscamos desde el repositories.py TODOS los favoritos del usuario (variable 'user').
        mapped_favourites = [repositories.saveFavourite(images)]

        for favourite in favourite_list:
            card = __hash__(favourite) # transformamos cada favorito en una Card, y lo almacenamos en card.
            mapped_favourites.append(card)

        return mapped_favourites

def deleteFavourite(request):
    favId = request.POST.get('id')
    return repositories.deleteFavourite(favId) # borramos un favorito por su ID.
