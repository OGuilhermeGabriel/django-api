#importe o viewsets
from rest_framework import viewsets, generics
#importe os modelos que serão utilizados
from escola.models import Aluno, Curso, Matricula
#importe os serializers
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListandoAlunosMatriculadosSerializer
#importe o pacote de autenticação básico
from rest_framework.authentication import BasicAuthentication
#importe a permissão de autenticação
from rest_framework.permissions import IsAuthenticated

#ModelViewSet => vizualiza todas as requisições executáveis por recurso
#ListAPIView => serve apenas para listar os viewsets

#Viewset para exibir todos os alunos(as)
class AlunosViewSet(viewsets.ModelViewSet):
    '''Listando todos os alunos e alun''' #mensagem que aparecerá na API ao acessar '/alunos'
    #trazendo todos os alunos com base no model para a variável "queryset"
    queryset = Aluno.objects.all()
    #chame o serializer respectivo do modelo relacionado ao viewset
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

#Viewset para exibir todos os cursos
class CursosViewSet(viewsets.ModelViewSet):
    '''Listando todos os cursos'''
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

#Viewset para exibir todas as matriculas
class MatriculasViewSet(viewsets.ModelViewSet):
    '''Listando todas as matrículas'''
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

#ListAPIView para listar as matrículas de um aluno
class ListaMatriculasAluno(generics.ListAPIView):
    '''Listando as matrículas de um aluno'''
    def get_queryset(self):
        #filtrar de todas as matrículas, a matrícula do aluno com o respectivo ID
        queryset = Matricula.objects.filter(aluno_id= self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

#ListAPIView para listar os alunos por curso
class ListaAlunosMatriculados(generics.ListAPIView):
    '''Listando os alunos e alunas matriculados em um curso'''
    def get_queryset(self):
        #filtrar de todos os alunos, os alunos com a matrícula respectiva ao ID
        queryset = Matricula.objects.filter(curso_id= self.kwargs['pk'])
        return queryset
    serializer_class = ListandoAlunosMatriculadosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]