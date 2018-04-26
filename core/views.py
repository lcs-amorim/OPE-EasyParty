from django.shortcuts import render, redirect , HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.views.generic import View, TemplateView, CreateView, UpdateView
from django.conf import settings 
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime

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

def login(request):
	return render(request,"login.html")
#Auntenticação Usuario

@login_required(login_url="entrar")
def page_user(request):
	return render(request,'index.html')
# Create your views here.
