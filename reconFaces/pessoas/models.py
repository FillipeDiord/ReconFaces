from django.db import models
import os

## função que retorna o nome da pessoa para que a imagem fique com o nome da pessoa
def salvar_imagem(instance, filename):

    dir = os.listdir('media/fotos/')

    instance.numero = 1

    ## verifica se tem imagens salvas para essa pessoa se estiver verifica qual foto foi apaga e passa o numero dela
    ## paga que a imagem seja salva
    if(dir) :

        for pessoa in dir:
            if instance.nome == pessoa:
                fotosAntigas = os.listdir('media/fotos/' + instance.nome + "/")

                for num,foto in enumerate(fotosAntigas):
                    instance.numero = ultimoNumeroFoto(instance.nome) + 1

                    f = foto.split('.')
                    n = int(f[1])

                    if num > n:
                        instance.numero = num

    nomeArquivo = filename.split(".")

    return 'fotos/'+instance.nome+ '/'+instance.nome+ '.' + str(instance.numero)+ '.' + nomeArquivo[1]

def ultimoNumeroFoto(nome):
    fotosAntigas = os.listdir('media/fotos/' + nome + "/")
    f = fotosAntigas[fotosAntigas.__len__() - 1].split('.')
    n = int(f[1])

    return n


class Pessoa(models.Model):
    nome = models.CharField(max_length=30)
    email = models.CharField(max_length=120)
    cpf = models.CharField(max_length=11)
    celular = models.CharField(max_length=11)
    idade = models.IntegerField()
    numero = 0
    foto1 = models.ImageField(upload_to=salvar_imagem)
    foto2 = models.ImageField(upload_to=salvar_imagem)
    foto3 = models.ImageField(upload_to=salvar_imagem)
    foto4 = models.ImageField(upload_to=salvar_imagem)
    foto5 = models.ImageField(upload_to=salvar_imagem)
    foto6 = models.ImageField(upload_to=salvar_imagem)

    def __str__(self):
        return self.nome


class Contagem(models.Model):
    identificadas = models.IntegerField()

    def __str__(self):
        return self.identificadas


