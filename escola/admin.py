from django.contrib import admin
from escola.models import Aluno, Curso

#classe para manter os alunos no admin
class Alunos(admin.ModelAdmin):
    #campos que serão exibidos no display do admin
    list_display = ('id','nome','rg','cpf','data_nascimento')
    #campos para clicar e alterar
    list_display_links = ('id','nome')
    #campos de busca
    search_fields = ('nome',)
    #paginação da quantidade de alunos
    list_per_page = 20

#registrar a configuração feita do model 'Aluno' baseado na classe do admin 'Alunos'
admin.site.register(Aluno, Alunos)

#classe para manter os cursos no admin
class Cursos(admin.ModelAdmin):
    list_display = ('id','codigo_curso','descricao')
    list_display_links = ('id','codigo_curso')
    search_fields = ('codigo_curso',)

admin.site.register(Curso, Cursos)