# Generated by Django 4.1.5 on 2023-03-17 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0004_contato_identidade_back_contato_identidade_front'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='cpf',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='contato',
            name='email',
            field=models.EmailField(blank=True, max_length=255),
        ),
    ]
