#importe os serializers
from rest_framework import serializers
#importe os models do app
from escola.models import Aluno, Curso, Matricula

#classe para serializar a model "aluno" => transformar a model(django) para json(api)
class AlunoSerializer(serializers.ModelSerializer):
    #classe meta = > comporta os metados que serão serializados (model, campos da model)
    class Meta:
        #model que será utilizado como base para o serializer
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
    #curso será um campo só de leitura e irá exibir o parametro de descricao dele (que mostra o nome) => trazendo o atributo "descricao" da model "curso" para a variável "curso" 
    curso = serializers.ReadOnlyField(source= 'curso.descricao')
    #para que o periodo "N", seja exibido como "noturno" por meio do método do serializer "get_periodo"
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        #em fields, não precisa exibir o nome do aluno uma vez que você já clicou no aluno
        fields = ['curso','periodo']
    #método para retornar o período uma instância de um curso qualquer, só que definido da mesma forma que foi no admin (admin = Noturno | "N" => "Noturno") 
    def get_periodo(self,obj):
        return obj.get_periodo_display()

#serializer para listar os alunos de cada curso 
class ListandoAlunosMatriculadosSerializer(serializers.ModelSerializer):
    #trazendo o nome do aluno, da classe "Aluno" para a variável "aluno_nome"
    aluno_nome = serializers.ReadOnlyField(source= 'aluno.nome')
    class Meta:
        model = Matricula
        fields = ['aluno_nome']