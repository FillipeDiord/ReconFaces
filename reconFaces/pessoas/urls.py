from django.urls import path
from .views import listar
from .views import nova
from .views import alterar
from .views import deletar
from .views import reconhecimento
from .views import listarContagem

urlpatterns = [
    path('listar/', listar, name="pessoa_listar"),
    path('nova/', nova, name="pessoa_nova"),
    path('alterar/<int:id>/', alterar, name="pessoa_alterar"),
    path('deletar/<int:id>/', deletar, name="pessoa_deletar"),
    path('reconhecimento/', reconhecimento, name='pessoa_reconhecimento'),
    path('contagem/',listarContagem , name="pessoa_contagem"),
]
