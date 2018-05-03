from django.shortcuts import render, redirect , HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.views.generic import View, TemplateView, CreateView, UpdateView
from django.conf import settings 
from django.shortcuts import render
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

def contato(request):
	return render(request,"contato.html")
#Auntenticação Usuario


# pagina de cadastro de jogador
def registrar(request):    
 	 # Se dados forem passados via POST
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid(): # se o formulario for valido
            form.save() # cria um novo usuario a partir dos dados enviados 
            return HttpResponseRedirect("/login/") # redireciona para a tela de login
        else:
            # mostra novamente o formulario de cadastro com os erros do formulario atual
            return render(request, "registrar.html", {"form": form})
    
    # se nenhuma informacao for passada, exibe a pagina de cadastro com o formulario
    return render(request, "registrar.html", {"form": UserCreationForm() })

@login_required(login_url="entrar")
def page_user(request):
	return render(request,'index.html')
# Create your views here.
