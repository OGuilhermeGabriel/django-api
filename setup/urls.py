from django.contrib import admin
from django.urls import path, include
#importar as viewsets
from escola.views import AlunosViewSet, CursosViewSet, MatriculasViewSet, ListaMatriculasAluno
#importar rota default do django rest
from rest_framework import routers

#definindo a rota default/principal
router = routers.DefaultRouter()
#registrando as viewsets em router: (nome de registro, Viewset, nome de visualização)
#ROTAS
router.register('alunos', AlunosViewSet, basename= 'Alunos')
router.register('cursos', CursosViewSet, basename= 'Cursos')
router.register('matriculas', MatriculasViewSet, basename= 'Matrículas')

urlpatterns = [
    #pra um 'admin/' na url => redireciona pro site do admin
    path('admin/', admin.site.urls),
    #pra um '' na url => redireciona o site para as rotas registradas no router  
    path('', include(router.urls)),
    path('aluno/<int:pk>/matriculas/', ListaMatriculasAluno.as_view()),
]