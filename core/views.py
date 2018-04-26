from django.shortcuts import render, redirect , HttpResponseRedirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.views.generic import View, TemplateView, CreateView, UpdateView
from django.conf import settings 
from django.contrib.auth.mixins import LoginRequiredMixin
#from django.contrib.auth import get_user_model


from django.shortcuts import render
from core.models import Produto
from core.models import Categoria



def index(request):
	contexto = {
		"produtos":Produto.objects.all()
	}
	return render(request, "index.html", contexto)		

def categorias(request):
	contexto = {
		"categorias":Categoria.objects.all()
	}
	return render(request, "index.html", contexto)	

def detalhe_produto(request, slug):
    contexto = {
        'produto': get_object_or_404(Produto, slug=slug) #verifica se a url existe, caso nao exista ele retorna erro 404
    }
    template_name = 'detalhe_produto.html'
    return render(request, template_name, contexto)

def login(request):
	return render(request,"login.html")
#Auntenticação Usuario

@login_required(login_url="entrar")
def page_user(request):
	return render(request,'index.html')
# Create your views here.
