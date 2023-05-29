from django.shortcuts import render

from app.models import Marca

TEMPLATE_BASE = "main/base.html"


# Create your views here.
def index(request):
    marcas = Marca.objects.all()
    return render(request, TEMPLATE_BASE, {'marcas': marcas})
