from django.shortcuts import render
# importar el modulo HttpResponse, nos pertime contestar a una peticion devolviendo un codigo
from django.shortcuts import HttpResponse
# Create your views here.

# CREAMOS LAS RUTAS
'''
    creamos una vista con una funcion ,
    devolviendo la respuesta con un codigo HTML que estan en el template
'''
def home(request):
    return render(request,'core/home.html')
def acerca_de(request):
    return render(request,'core/acerca_de.html')
def contacto(request):
    return render(request,'core/contacto.html')
def portafolio(request):
    return render(request,'core/portafolio.html')