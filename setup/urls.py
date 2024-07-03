from django.contrib import admin
from django.urls import path, include
#importar as viewsets
from escola.views import AlunosViewSet, CursosViewSet
#importar rota default do django rest
from rest_framework import routers

#definindo a rota default/principal
router = routers.DefaultRouter()
#registrando as viewsets em router
router.register('alunos', AlunosViewSet, basename= 'Alunos')
router.register('cursos', CursosViewSet, basename= 'Cursos')

urlpatterns = [
    #pra um 'admin/' na url => redireciona pro site do admin
    path('admin/', admin.site.urls),
    #pra um '' na url => redireciona o site para as rotas registradas no router  
    path('', include(router.urls)),
]