from django.shortcuts import render
from core.models import Usuario

def index(request):
	return render(request, "index.html")		

def Produto(request):
	contexto = {
		"users":Usuario.objects.all()
	}
	return render(request,"index.html", contexto)

# Create your views here.
