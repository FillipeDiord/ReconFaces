import os
import shutil

## apaga a pasta de fotos
def apagar_arquivos(nome):

  ## exclui as fotos
  dir = os.path.dirname('media/fotos/'+str(nome)+'/')
  shutil.rmtree(dir)

  ## exclui os treinamentos
  apagar_treinamento()

# apaga a foto e os arquivos de treinamento
def apagar_foto(nome, foto):

  ## exclui a foto do diretorio
  dir = os.path.dirname('media/fotos/' + str(nome) + '/')
  print("Excluindo a foto "+dir+"/"+foto)
  os.remove(dir+"/"+foto)

# função que apagar os treinamento
def apagar_treinamento() :
  dirs = os.listdir('media/treinamento/')

  if dirs.__len__() > 0:
     dir = 'media/treinamento/'

     os.remove(dir + "/descritores.npy")
     os.remove(dir + "/indices.pickle")
