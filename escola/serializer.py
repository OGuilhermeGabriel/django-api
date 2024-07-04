#importe os serializers
from rest_framework import serializers
#importe os models do app
from escola.models import Aluno, Curso, Matricula

#classe para serializar a model "aluno" => transformar a model(django) para json(api)
class AlunoSerializer(serializers.ModelSerializer):
    #classe meta = > comporta os metados que serão serializados (model, campos da model)
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']

#serializer do model do Curso
class CursoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Curso 
        #todos os campos/atributos da model que define os cursos 
        fields = '__all__'

#serializer do model da Matrícula 
class MatriculaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Matricula
        #trás todos os campos menos os específicos dentro da lista 
        exclude = []

#serializer para listar as matrículas de cada aluno
class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        #em fields, não precisa exibir o nome do aluno uma vez que você já clicou no aluno
        fields = ['curso','periodo']