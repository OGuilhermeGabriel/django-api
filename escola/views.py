from django.http import JsonResponse

def alunos(request):
    #se o método de requisição dessa função for GET, retorna um arquivo que contem as variáveis de aluno
    if request.method == 'GET':
        aluno = {'id':1, 'nome':'Guilherme'}
        return JsonResponse(aluno)
