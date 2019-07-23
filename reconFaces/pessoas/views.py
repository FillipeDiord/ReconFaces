import os

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from reconhecimento.reconhecimento import Reconhecimento
from .models import Pessoa, Contagem
from .forms import PersonForm

from reconhecimento.treinamento import Treinamento
from pessoas.arquivos import apagar_arquivos, apagar_foto, apagar_treinamento

import threading

@login_required
def listar(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'lista.html', {'pessoas': pessoas})

def nova(request):
    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()

        ## se houver um treinamento  apaga o treinamento
        dir = os.listdir('media/treinamento/')
        if dir.__len__() > 0:
         apagar_treinamento()

        ## abre uma nova thread para fazer o treinamento das pessoas
        treinamento = Treinamento()
        th = threading.Thread(target=treinamento.gerarTreinamento)
        th.start()

        return redirect('pessoa_listar')

    return render(request, 'pessoa_form.html', {'form': form})

## função que auxilia a verificação das fotos
def verificar(request, nome):

     for foto in request.FILES:
         n = int(foto.split('foto')[1])
         verificaFotoAtualComAntiga(nome, foto, (n-1))

     ## apos verificar as fotos exclui o treinamento caso tenha uma foto novo
     if request.FILES:
         ## se houver um treinamento  apaga o treinamento
         dir = os.listdir('media/treinamento/')
         if dir.__len__() > 0:
           apagar_treinamento()

## função que recebe a foto atual e verifica se a mesma é diferente das antigas se for apaga a antiga
def verificaFotoAtualComAntiga(nome, fotoAtual, numeroFoto):

    fotosAntigas = os.listdir('media/fotos/'+nome+"/")

    for pos,foto in enumerate(fotosAntigas):
        f = foto.split('.')
        n = int(f[1])

        if numeroFoto == n:
            numeroFoto = pos
            break

    fotoAntiga = fotosAntigas[numeroFoto]

    if fotoAntiga != fotoAtual:
        apagar_foto(nome, fotoAntiga)

@login_required
def alterar(request, id):
    pessoa = get_object_or_404(Pessoa, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=pessoa)

    nome_antigo = pessoa.nome

    if form.is_valid():
        ## verifica as imagens antes de alterar
        verificar(request, pessoa.nome)

        form.save()

        ## apaga o arquivo de treinamento e refaz o treinamento
        if nome_antigo != request.POST.get('nome'):

            dir = os.listdir('media/treinamento/')
            if dir.__len__() > 0:
              apagar_treinamento()

            ## abre uma nova thread para fazer o treinamento das pessoas
            treinamento = Treinamento()
            th = threading.Thread(target=treinamento.gerarTreinamento)
            th.start()

        ## gera um novo treinamento caso mude uma foto
        if request.FILES:
            ## abre uma nova thread para fazer o treinamento das pessoas
            treinamento = Treinamento()
            th = threading.Thread(target=treinamento.gerarTreinamento)
            th.start()

        return redirect('pessoa_listar')

    return render(request, 'pessoa_form.html', {'form': form, 'pessoa': pessoa})

@login_required
def deletar(request, id):
    pessoa = get_object_or_404(Pessoa, pk=id)

    if request.method == 'POST':
        pessoa.delete()

        ## após remover a pessoa exclui suas fotos e seus arquivos de treinamento
        apagar_arquivos(pessoa.nome)

        ## só realiza o treinamento se houver uma foto dessa pessoa
        dirs = os.listdir('media/fotos/')
        if dirs.__len__() > 0:
          ## abre uma nova thread para fazer o treinamento das pessoas
          treinamento = Treinamento()
          th = threading.Thread(target=treinamento.gerarTreinamento)
          th.start()

        return redirect('pessoa_listar')

    return render(request, 'pessoa_delete_confirm.html', {'pessoa': pessoa})

def reconhecimento(request):
  recon = Reconhecimento()
  recon.indentificar()

  return redirect('pessoa_listar')

def listarContagem(request):
    contagem = Contagem.objects.all()
    return render(request, 'contagem.html', {'contagem': contagem[0]})