from django.urls import path, include
from .views import index, estante, contacto, agregar_comic, listar_comic,\
      modificar_comic, eliminar_comic, registro #ComicViewset , EditorialSerializer
from rest_framework import routers


#router = routers.DefaulRouter()
#router.regiter("comic",ComicViewset)
#router.register('editorial', EditorialViewset)

urlpatterns = [
    path('', index, name="index"),
    path('estante/', estante, name="estante"),
    path('contacto/', contacto, name="contacto"),
    path('agregar-comic/', agregar_comic, name="agregar_comic"),
    path('listar-comic/', listar_comic, name="listar_comic"),
    path('modificar-comic/<id>', modificar_comic, name="modificar_comic"),
    path('eliminar-comic/<id>',eliminar_comic, name="eliminar_comic"),
    path('registro/', registro, name="registro"),
   # path('api/', include(router.urls)), 
   # #Quise implementar la api pero me marca error lo dejo en comentario para que la paguina funcione
]
