#importe os serializers
from rest_framework import serializers
#importe os models do app
from escola.models import Aluno, Curso

#classe para serializar a model "aluno" => transformar a model(django) para json(api)
class AlunoSerializer(serializers.ModelSerializer):
    #classe meta = > comporta os metados que serão serializados (model, campos da model)
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']

class CursoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Curso 
        #todos os campos/atributos da model que define os cursos 
        fields = '__all__'