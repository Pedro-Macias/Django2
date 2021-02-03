from django.shortcuts import render
from .models import Proyecto
# Create your views here.

def portafolio(request):
    proyectos = Proyecto.objects.all()
    return render(request,'portafolio/portafolio.html',{'proyectos':proyectos})