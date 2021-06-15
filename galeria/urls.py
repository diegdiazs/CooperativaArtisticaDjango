from django.urls import path
from .views import form_obradearte , form_mod_obradearte, form_del_obradearte
from .views import home
from .views import contacto
from .views import exposiciones
from .views import fotografia
from .views import iniciosesion
from .views import registro

urlpatterns = [
    path('', home, name="home"),
    path('contacto',contacto,name='contacto'),
    path('exposiciones',exposiciones,name='exposiciones'),
    path('fotografia',fotografia,name='fotografia'),
    path('iniciosesion',iniciosesion,name='iniciosesion'),
    path('registro',registro,name='registro'),
    path('agregar-obradearte',form_obradearte,name='form_obradearte'),
    path('modificar-obradearte/<id>',form_mod_obradearte,name='form_mod_obradearte'),
    path('borrar-obradearte/<id>',form_del_obradearte,name='form_del_obradearte'),

]