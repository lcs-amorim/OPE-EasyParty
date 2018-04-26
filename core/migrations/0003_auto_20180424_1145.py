# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-24 14:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_categoria_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='descricao',
            field=models.TextField(db_column='Descricao_P', verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(db_column='Imagem', upload_to='media', verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='nome_f',
            field=models.ForeignKey(db_column='Nome Fornecedor', on_delete=django.db.models.deletion.DO_NOTHING, to='core.Fornecedor'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='nome_p',
            field=models.CharField(db_column='Nome_P', max_length=100, verbose_name='Nome do produto'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='quantidade',
            field=models.SmallIntegerField(db_column='Quantidade', verbose_name='Quantidade'),
        ),
    ]