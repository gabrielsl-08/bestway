from django import forms
from .models import Aluno, Frequencia, Professor

print(Aluno.objects.all())
class AlunoForm (forms.ModelForm):
    class Meta:
        model = Aluno  # O modelo base para o formulário
        fields = ['nome', 'idade','data_nascimento', 'sexo', 'cpf', 'telefone','rua','numero','bairro','cidade','cep','faixa', 'email', 'responsavel','polo','turma',]  # Campos que serão exibidos no formulário

        widgets = {
            
            'sexo': forms.Select(),  # Um select dropdown para o campo sexo
            'cpf': forms.TextInput(attrs={'maxlength': 11, 'pattern': '[0-9]+', 'title': 'Digite apenas números'}),
            'telefone': forms.TextInput(attrs={'maxlength': 15, 'pattern': '[0-9]+', 'title': 'Digite apenas números'}),
        }


class FrequenciaForm(forms.ModelForm):
    class Meta:
        model = Frequencia
        fields = ['aluno', 'turma', 'professor', 'polo', 'presente']


class FiltroFrequenciaForm(forms.Form):
    turma = forms.ChoiceField(
        choices=[('', 'Todas as Turmas')] + Aluno.TURMA_CHOICES,
        required=False,
        label="Turma"
    )
    polo = forms.ChoiceField(
        choices=[('', 'Todos os Polos')] + Aluno.POLO_CHOICES,
        required=False,
        label="Polo"
    )

  
