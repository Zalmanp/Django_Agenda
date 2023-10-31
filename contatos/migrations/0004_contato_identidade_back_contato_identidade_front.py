# Generated by Django 4.1.5 on 2023-03-17 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0003_contato_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='identidade_back',
            field=models.ImageField(blank=True, upload_to='fotos/%Y/%m/'),
        ),
        migrations.AddField(
            model_name='contato',
            name='identidade_front',
            field=models.ImageField(blank=True, upload_to='fotos/%Y/%m/'),
        ),
    ]