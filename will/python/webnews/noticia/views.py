from django.shortcuts import render
from .models import Autor
from .forms import AutorForm

# Create your views here.

def home(request):
    return render(request, 'home.html')


def listar(request):
    autores = Autor.objects.all().order_by("nome")
    return render(request, 'listar.html', {"autores": autores})

def detalhar(request, id):
    autor = Autor.objects.get(id=id)
    return render(request, 'detalhar.html', {"autor": autor})

def cadastrar(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home.html')

    else:
        form = AutorForm()
        return render(request, 'cadastrar.html', {'form': form})
    
def atualizar(request, id):
    autor = Autor.objects.get(id=id)
    form = AutorForm(instance=autor)
        
        
