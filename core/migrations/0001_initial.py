# Generated by Django 2.0.3 on 2018-03-15 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colaboradores',
            fields=[
                ('nome_c', models.CharField(db_column='Nome_C', max_length=100)),
                ('codigo_c', models.AutoField(db_column='Codigo_C', primary_key=True, serialize=False)),
                ('telefone_c', models.IntegerField(db_column='Telefone_C')),
            ],
            options={
                'managed': False,
                'db_table': 'Colaboradores',
            },
        ),
        migrations.CreateModel(
            name='Contratos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(db_column='Descricao')),
                ('dia', models.DateField(db_column='Dia')),
                ('hora', models.TimeField(db_column='Hora')),
                ('endereco_ct', models.CharField(db_column='Endereco_CT', max_length=100)),
            ],
            options={
                'managed': False,
                'db_table': 'Contratos',
            },
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('nome_f', models.CharField(db_column='Nome_F', max_length=100, primary_key=True, serialize=False)),
                ('email_f', models.CharField(blank=True, db_column='Email_F', max_length=100, null=True)),
                ('endereco_f', models.CharField(db_column='Endereco_F', max_length=255)),
                ('telefoneprincipal', models.IntegerField(db_column='TelefonePrincipal')),
                ('telefonesecundario', models.IntegerField(blank=True, db_column='TelefoneSecundario', null=True)),
                ('categoria_f', models.CharField(db_column='Categoria_F', max_length=100)),
            ],
            options={
                'managed': False,
                'db_table': 'Fornecedor',
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('codigo_p', models.AutoField(db_column='Codigo_P', primary_key=True, serialize=False)),
                ('nome_p', models.CharField(db_column='Nome_P', max_length=100)),
                ('quantidade', models.SmallIntegerField(db_column='Quantidade')),
                ('categoria_p', models.CharField(db_column='Categoria_P', max_length=100)),
            ],
            options={
                'managed': False,
                'db_table': 'Produto',
            },
        ),
        migrations.CreateModel(
            name='Sysdiagrams',
            fields=[
                ('name', models.CharField(max_length=128)),
                ('principal_id', models.IntegerField()),
                ('diagram_id', models.AutoField(primary_key=True, serialize=False)),
                ('version', models.IntegerField(blank=True, null=True)),
                ('definition', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'sysdiagrams',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('codigo_u', models.AutoField(db_column='Codigo_U', primary_key=True, serialize=False)),
                ('nome_u', models.CharField(db_column='Nome_U', max_length=255)),
                ('usuario', models.CharField(db_column='Usuario', max_length=100, unique=True)),
                ('senha', models.CharField(db_column='Senha', max_length=100)),
                ('email_u', models.CharField(blank=True, db_column='Email_U', max_length=100, null=True)),
                ('cpf', models.IntegerField(db_column='CPF', unique=True)),
                ('telefone_u', models.IntegerField(db_column='Telefone_U')),
                ('endereco_u', models.CharField(db_column='Endereco_U', max_length=255)),
                ('news', models.NullBooleanField(db_column='News')),
            ],
            options={
                'managed': False,
                'db_table': 'Usuario',
            },
        ),
    ]
