# Generated by Django 4.2.16 on 2024-11-27 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0004_alter_aluno_telefone'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='polo',
            field=models.CharField(blank=True, choices=[('itatinga', 'Itatinga'), ('enseada', 'Enseada'), ('barequecaba', 'Barequeçaba'), ('boraceia', 'Boraceia')], max_length=15, null=True),
        ),
    ]
