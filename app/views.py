from django.shortcuts import render

from app.models import Marca

TEMPLATE_BASE = "main/base.html"
TEMPLATE_SOBRE = "main/sobre.html"


# Create your views here.
def index(request):
    marcas = Marca.objects.all()
    return render(request, TEMPLATE_BASE, {'marcas': marcas})


def sobre(request):
    return render(request, TEMPLATE_SOBRE)
