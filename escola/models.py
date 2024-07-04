from django.db import models

#Para lidar com os alunos
class Aluno(models.Model):
    nome = models.CharField(max_length= 30)
    rg = models.CharField(max_length= 9)
    cpf = models.CharField(max_length= 11)
    data_nascimento = models.DateField(max_length= 30)

    #representar o obj da classe "aluno" como str do atributo 'nome'
    def __str__(self):
        return self.nome
    
#Para lidar com os cursos
class Curso(models.Model):
    #tipo do curso: básico, intermediário, avançado
    #No banco de dados serão aplicados serão salvos apenas as letra do nível B I e A
    NIVEL = (
        ('B','Básico'),
        ('I','Intermediário'),
        ('A','Avançado'),
    )

    codigo_curso = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(max_length= 1, choices= NIVEL, blank= False, null= False, default= 'B')

    #representar o obj da classe "curso" como str do atributo 'descricao'
    def __str__(self):
        return self.descricao

class Matricula(models.Model):
    #Criando período novamente baseado na lógica "choices"
    PERIODO = (
        ('M','Matutino'),
        ('V','Vespertino'),
        ('N','Noturno')
    )
    #atributos vindos de outras classes/models => Aluno & Curso
    '''
    models.ForeignKey(classe, <other_methods>)
    'on_delete= models.CASCADE' => quando a instância da classe/model aluno ou curso (um objeto aluno ou curso) for deletada, a matrícula relaciona a este aluno também será deletada.  
    '''
    aluno = models.ForeignKey(Aluno, on_delete= models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete= models.CASCADE)
    #atributo de período
    periodo = models.CharField(max_length=1, choices= PERIODO, blank= False, null= False, default= 'M')