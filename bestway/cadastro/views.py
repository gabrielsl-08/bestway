
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import AlunoForm, FrequenciaForm, FiltroFrequenciaForm
from .models import Aluno, Frequencia, Professor


def cadastrar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro efetuado com sucesso!')
    else:
        form = AlunoForm()
    
    return render(request, 'cadastrar_aluno.html', {'form': form})
    
 
def index(request):
    return render (request, 'index.html')



def listar_frequencias(request):
    frequencias = Frequencia.objects.select_related('aluno', 'professor').order_by('-data')
    return render(request, 'listar_frequencias.html', {'frequencias': frequencias})



def frequencia(request):
    alunos = Aluno.objects.all()  # Inicialmente, lista todos os alunos
    form = FiltroFrequenciaForm(request.GET or None)

    # Filtrar os alunos se os filtros forem enviados
    if form.is_valid():
        turma = form.cleaned_data.get('turma')
        polo = form.cleaned_data.get('polo')

        if turma:
            alunos = alunos.filter(turma=turma)
        if polo:
            alunos = alunos.filter(polo=polo)

    # Processar a frequência
    if request.method == 'POST':
        for aluno_id, status in request.POST.items():
            if aluno_id.startswith('presenca_'):
                aluno_id = aluno_id.split('_')[1]
                presente = status == 'on'
                Frequencia.objects.create(aluno_id=aluno_id, presente=presente)

        return redirect('frequencia')  # Redirecionar para a mesma página após salvar

    return render(request, 'frequencia.html', {'form': form, 'alunos': alunos})

