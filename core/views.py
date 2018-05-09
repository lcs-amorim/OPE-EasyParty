from django.shortcuts import render, redirect , HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.views.generic import View, TemplateView, CreateView, UpdateView
from django.conf import settings 
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from core.forms import ClienteForm


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


def checa_cliente(usuario):
    return usuario.perfil == "cliente"

def checa_colaborador(usuario):
    return usuario.perfil == "colaborador"

def checa_adm(usuario):
    return usuario.perfil == "ADM"  


@login_required(login_url="entrar")
@user_passes_test(checa_cliente)
def aluno(request):
    return render(request, "aluno.html")

@login_required(login_url="entrar")
@user_passes_test(checa_colaborador)
def professor(request):
    return render(request, "professor.html")

@login_required(login_url="entrar")
@user_passes_test(checa_adm)
def coordenador(request):
    return render(request, "coordenador.html") 



#Auntenticação Usuario
@login_required(login_url="entrar")
def page_user(request):
	return render(request,'index.html')

    # pagina de cadastro
def registrar(request):    
     # Se dados forem passados via POST
    if request.POST:
        form = ClienteForm(request.POST)
        if form.is_valid(): # se o formulario for valido
            form.save() # cria um novo usuario a partir dos dados enviados
    else:
        form = ClienteForm()
    contexto = {
        "form":form
    }
    return render(request, "registrar.html", contexto)
