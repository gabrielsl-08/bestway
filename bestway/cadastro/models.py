from django.db import models

# Create your models here.


class Aluno(models.Model):
    POLO_CHOICES = [
        ('itatinga', 'Itatinga'),
        ('enseada', 'Enseada'),
        ('barequecaba', 'Barequeçaba'),
        ('boraceia', 'Boraceia'),
    ]

    TURMA_CHOICES = [
        ('infantil', 'Infantil'),
        ('juvenil', 'Juvenil'),
        ('adulto', 'Adulto'),
    ]

    SEXO_CHOICES = [
        ('M','Masculino'),
        ('F','Femenino'),
    ]
    FAIXA_CHOICES = [
        ('branca', 'Branca'),
        ('branca_cinza', 'Branca e Cinza'),
        ('cinza', 'Cinza'),
        ('cinza_preta', 'Cinza e Preta'),
        ('amarela_branca', 'Amarela e Branca'),
        ('amarela', 'Amarela'),
        ('amarela_preta', 'Amarela e Preta'),
        ('laranja_branca', 'Laranja e Branca'),
        ('laranja', 'Laranja'),
        ('laranja_preta', 'Laranja e Preta'),
        ('verde_branca', 'Verde e Branca'),
        ('verde', 'Verde'),
        ('verde_preta', 'Verde e Preta'),
        ('azul', 'Azul'),
        ('roxa', 'Roxa'),
        ('marrom', 'Marrom'),
        ('preta', 'Preta'),
    ]

    nome = models.CharField(max_length=50)
    idade =  models.PositiveIntegerField()
    data_nascimento = models.DateField(blank=True, null=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    cpf = models.PositiveIntegerField()
    telefone = models.PositiveIntegerField(max_length=11,unique=True)
    rua = models.CharField(max_length=20,blank=True, null=True)
    numero = models.CharField(max_length=4, blank=True, null=True)
    bairro = models.CharField(max_length=20,blank=True, null=True)
    cidade = models.CharField(max_length=20,blank=True, null=True)
    cep = models.CharField(max_length=9,blank=True, null=True)
    email = models.EmailField (unique=True)
    faixa = models.CharField(max_length=20, choices=FAIXA_CHOICES,blank=True, null=True)
    responsavel = models.CharField(max_length=50, blank=True, null=True)
    turma = models.CharField(max_length=10, choices=TURMA_CHOICES,blank=True, null=True)  # Campo para turma
    polo = models.CharField(max_length=15, choices=POLO_CHOICES, blank=True, null=True)  # Novo campo

    def __str__(self):# mostra a classe na área do admistrador
        return self.nome

class Professor(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)
    cpf = models.CharField(max_length=11, unique=True,blank=True, null=True)    
    telefone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True,blank=True, null=True)

    
    class Meta: verbose_name_plural = 'Professores'
    def __str__(self):
        return self.nome    
    

class Administrador(models.Model):
    
    class Meta: verbose_name_plural = 'Administradores'
    def __str__(self):
        return self.nome  

class Frequencia(models.Model):
    POLO_CHOICES = [
        ('itatinga', 'Itatinga'),
        ('enseada', 'Enseada'),
        ('barequecaba', 'Barequeçaba'),
        ('boraceia', 'Boraceia'),
    ]

    aluno = models.ForeignKey('Aluno', on_delete=models.CASCADE, related_name='frequencias')
    turma = models.CharField(max_length=10, choices=Aluno.TURMA_CHOICES)
    professor = models.ForeignKey('Professor', on_delete=models.SET_NULL, null=True, related_name='frequencias')
    polo = models.CharField(max_length=15, choices=POLO_CHOICES)  # Novo campo
    data = models.DateField(auto_now_add=True)
    presente = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.aluno.nome} - {self.turma} - {self.polo} - {self.data} - {'Presente' if self.presente else 'Ausente'}"
