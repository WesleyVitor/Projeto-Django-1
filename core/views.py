from django.shortcuts import render
from django.contrib import messages

from .forms import ContatoForm, ProdutoModelForm

from .models import Produto
# Create your views here.


def index(request):
    context = {
        "produtos":Produto.objects.all()
    }
    return render(request, 'index.html', context)


def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()
            messages.success(request, 'Email Enviado com sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar o email!')


    context ={
        'form': form
    }
    return render(request, 'contato.html', context)


def produto(request):
    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Produto salvo com sucesso.")
            form = ProdutoModelForm()
        else:
            messages.error(request, "Erro ao salvar Produto.")
    else:
        form = ProdutoModelForm()
    
    context = {
        "form":form
    }
    return render(request, 'produto.html', context)

