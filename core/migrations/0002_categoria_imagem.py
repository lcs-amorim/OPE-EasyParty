# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-23 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='imagem',
            field=models.ImageField(db_column='Imagem', default=1, upload_to='media'),
            preserve_default=False,
        ),
    ]