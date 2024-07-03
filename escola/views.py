#importe o viewsets
from rest_framework import viewsets
#importe os modelos que serão utilizados
from escola.models import Aluno, Curso
#importe os serializers
from escola.serializer import AlunoSerializer, CursoSerializer

#Viewset para exibir todos os alunos(as)
class AlunosViewSet(viewsets.ModelViewSet):
    #trazendo todos os alunos com base no model para a variável "queryset"
    queryset = Aluno.objects.all()
    #chame o serializer respectivo do modelo relacionado ao viewset
    serializer_class = AlunoSerializer

#Viewset para exibir todos os cursos
class CursosViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer