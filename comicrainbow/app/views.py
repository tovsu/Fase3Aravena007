from django.shortcuts import render, redirect, get_object_or_404
from .models import Comic, Editorial
from.forms import ContactoForm, ComicForm, CustomUserCrationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets
from .serializers import ComicSerializer,EditorialSerializer
# Create your views here.

#class EditorialViewst(viewsets.ModelViewSet):
 #   queryset = Editorial.objects.all()
  #  serializer_class = EditorialSerializer

#class ComicViewset(viewsets.ModelViewSet):
    #queryset = Comic.objects.all()
    #serializer_class = ComicSerializer
    #def get_queryset(self):
     #  comics = Comic.objects.all()
     #  nombre = self.request.GET.get('nombre')
     # if nombre:
     #      comics = comics .filter(nombre__contains="nombre")
     #  return comics


def index(request):
    comics = Comic.objects.all()
    data = {
        'comics': comics
    }
    return render(request, 'app/index.html', data)

def estante(request):
    return render(request, 'app/estante.html')


def contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = 'contacto guardado'
        else:
            data["form"] = formulario

    return render(request, 'app/contacto.html', data)

@permission_required('app.add_comic')
def agregar_comic(request):

    data = {
        'form': ComicForm()
    }
    if request.method == 'POST':
        formulario = ComicForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success( request, "Comic agregado correctamente")
        else:
            data["form"] = formulario 
    
    return render(request, 'app/comic/agregar.html', data)

@permission_required('app.view_comic')
def listar_comic(request):
    comics = Comic.objects.all()
     
    
    data = {
        'comics': comics
        
    }
    return render(request, 'app/comic/listar.html', data)

@permission_required('app.change_comic')
def modificar_comic(request, id):
    comic = get_object_or_404(Comic, id=id)
    data = {
        'form': ComicForm(instance=comic)
    }
    if request.method == 'POST':
        formulario = ComicForm (data=request.POST, instance=comic, files=request.FILES )
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Comic Editado Correctamente")
            return redirect(to="listar_comic")
        data["form"] = formulario    
    return render(request, 'app/comic/modificar.html',data)

@permission_required('app.delete_comic')
def eliminar_comic(request, id):

    comic = get_object_or_404(Comic, id=id)
    comic.delete()
    messages.success(request, "Comic Eliminado Correctamente")
    return redirect(to="listar_comic")

def registro(request):
    data = {
        'form': CustomUserCrationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCrationForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], 
            password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "se a registrado sin ningunerror")
            return redirect(to="index")
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)