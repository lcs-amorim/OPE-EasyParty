from django.shortcuts import render, redirect , HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.views.generic import View, TemplateView, CreateView, UpdateView
from django.conf import settings 
from django.contrib.auth.mixins import LoginRequiredMixin

from core.forms import ClienteForm
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

def produto_unico(request, slug):
    contexto = {
        'produto': get_object_or_404(Produto, slug=slug) #verifica se a url existe, caso nao exista ele retorna erro 404
    }
    return render(request, 'produto_unico.html', contexto)

def login_cliente(request):
	return render(request,"login.html")

def contato(request):
	return render(request,"contato.html")


#Auntenticação Usuario
@login_required(login_url="entrar")
def page_user(request):
	return render(request,'index.html')

# -----------------------------------------------//---------------------------------#

# pagina de cadastro
def registrar(request):    
     # Se dados forem passados via POST
    if request.POST:
        form = ClienteForm(request.POST)
        if form.is_valid(): # se o formulario for valido
            form.save() # cria um novo usuario a partir dos dados enviados
            form.cleaner
    else:
        form = ClienteForm()
    contexto = {
        "form":form
    }
    return render(request, "registrar.html", contexto)


# -----------------------------------------------//---------------------------------#
