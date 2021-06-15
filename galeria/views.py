from typing import ContextManager
from django.http.request import HttpRequest
from django.shortcuts import redirect, render
from .models import  Categoria, obradearte
from .forms import obradearteForm
# Create your views here.


def home(request):
    return render(request,'galeria/index.html')
#de aqui para abajo creamos los forms y crud con los datos 
def contacto(request):

    listaobra = obradearte.objects.all()
    datos = {
        'obradearte':listaobra,
    }
    return render(request,'galeria/contacto.html',datos)

def form_obradearte(request):

    datos = {

        'form':obradearteForm()

    }

    if(request.method == 'POST'):

        formulario = obradearteForm(request.POST)

        if formulario.is_valid():

            formulario.save()

            datos['mensaje'] = 'Guardados correctamente'

    return render(request,'galeria/form_obradearte.html',datos)

def form_mod_obradearte(request, id):
    obradeartee = obradearte.objects.get(añocreacion=id)
    
    datos = {
        'form':obradearteForm(instance=obradeartee)
    }

    if(request.method == 'POST'):
        formulario = obradearteForm(data=request.POST, instance=obradeartee)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Modificados correctamente'

    return render(request,'galeria/form_mod_obradearte.html',datos)

def form_del_obradearte(request, id):
    obradeartee = obradearte.objects.get(añocreacion=id)
    obradearte.delete()

    return redirect(to='home')



def exposiciones(request):
    return render(request,'galeria/exposiciones.html')

def fotografia(request):
    return render(request,'galeria/fotografia.html')

def iniciosesion(request):
    return render(request,'galeria/iniciosesion.html')

def registro(request):
    return render(request,'galeria/registro.html')


