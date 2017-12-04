from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.http import HttpResponseRedirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm  

from .models import Projeto
from .forms import ProjetoForm

from django.contrib.auth import authenticate, login,logout

def home(request):
    return render(request, "index.html", {"user": request.user})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST) # Veja a documentacao desta funcao
        
        if form.is_valid():
            #se o formulario for valido significa que o Django conseguiu encontrar o usuario no banco de dados
            #agora, basta login o usuario e ser feliz.
            login(request, form.get_user())
            return HttpResponseRedirect("/ps/") # redireciona o usuario logado para a pagina inicial
        else:
            return render(request, "login.html", {"form": form})
    
    #se nenhuma informacao for passada, exibe a pagina de login com o formulario
    return render(request, "login.html", {"form": AuthenticationForm()})

def registrar(request):
    # Se dados forem passados via POST
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid(): # se o formulario for valido
            form.save() # cria um novo usuario a partir dos dados enviados 
            return HttpResponseRedirect("/ps/login/") # redireciona para a tela de login
        else:
            # mostra novamente o formulario de cadastro com os erros do formulario atual
            return render(request, "registrar.html", {"form": form})
    
    # se nenhuma informacao for passada, exibe a pagina de cadastro com o formulario
    return render(request, "registrar.html", {"form": UserCreationForm() })

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/ps/login/")

class ProjetoListView(ListView):
    model = Projeto

def novo_projeto(request):
    # Se dados forem passados via POST
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        
        if form.is_valid(): # se o formulario for valido
            form.save() # cria um novo usuario a partir dos dados enviados 
            return HttpResponseRedirect("/ps/") # redireciona para a tela de login
        else:
            # mostra novamente o formulario de cadastro com os erros do formulario atual
            return render(request, "novo_projeto.html", {"form": form})
    
    # se nenhuma informacao for passada, exibe a pagina de cadastro com o formulario
    return render(request, "novo_projeto.html", {"form": ProjetoForm() })