from django.shortcuts import render
from .models import Service

# Create your views here.
def services(request):
    services=Service.objects.all() # Consulta para obtener todos los servicios
    return render(request,"services/services.html",{'listServices':services})