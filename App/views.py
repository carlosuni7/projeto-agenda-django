from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Contato
from .forms import ContatoModelForm

def index(request):

    lista = Contato.objects.all()
    print(lista)
    empresa = 'Carlitos Corp'
    context = {
        'lista': lista
    }
    return render(request, "index.html", context)


def usuarioContato(request, pk):

    contato = Contato.objects.get(id=pk)
    context = {
        'contato': contato
    }
    return render(request, "usuario.html", context)

def cadContato(request):

    if request.method == 'POST':
        form = ContatoModelForm(request.POST)

        if form.is_valid(): # OBRIGATORIO COLOCAR ESTE CONTROLE
            contato = form.save()
            form = ContatoModelForm()

            messages.success(request, 'Contato cadastrado com sucesso!')
            return redirect("/")
        else:
            messages.error(request, 'Erro ao cadastrar contato')
    else:
        form = ContatoModelForm()
    
    context = {
        'form': form
    }
    return render(request, 'cadContato.html', context)

def altContato(request, pk):

    contato = Contato.objects.get(id=pk)

    if request.method == 'POST':
        form = ContatoModelForm(request.POST, request.FILES, instance=contato)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = ContatoModelForm(instance=contato)
    context = {
        "form": form,
        "cont": contato
    }
    return render(request, "altContato.html", context)

def excContato(request, pk):

    contato = Contato.objects.get(id=pk)
    #print(contato)
    if request.method == 'POST':
        #form = ContatoModelForm(request.POST)
        #if form.is_valid():
            contato.delete()
            return redirect("/")

    context = {
        "contato": contato
    }

    return render(request, "excContato.html", context)