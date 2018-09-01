# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esocial', '0001_initial'),
        ('controle_de_acesso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='s1020alteracao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codlotacao', models.CharField(max_length=30)),
                ('inivalid', models.CharField(max_length=7, choices=[(b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('fimvalid', models.CharField(blank=True, max_length=7, null=True, choices=[(b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('tplotacao', models.CharField(max_length=2, choices=[(b'1', '01 - Classifica\xe7\xe3o da atividade econ\xf4mica exercida pela Pessoa Jur\xeddica para fins de atribui\xe7\xe3o de c\xf3digo FPAS, inclusive obras de constru\xe7\xe3o civil pr\xf3pria, exceto: a) empreitada parcial ou sub-empreitada de obra de constru\xe7\xe3o civil (utilizar op\xe7\xe3o 02); b) (...)'), (b'10', '10 - Embarca\xe7\xe3o inscrita no Registro Especial Brasileiro - REB'), (b'2', '02 - Obra de Constru\xe7\xe3o Civil - Empreitada Parcial ou Sub- empreitada'), (b'21', '21 - Classifica\xe7\xe3o da atividade econ\xf4mica ou obra pr\xf3pria de constru\xe7\xe3o civil da Pessoa F\xedsica'), (b'24', '24 - Empregador Dom\xe9stico'), (b'3', '03 - Pessoa F\xedsica Tomadora de Servi\xe7os prestados mediante cess\xe3o de m\xe3o de obra, exceto contratante de cooperativa'), (b'4', '04 - Pessoa Jur\xeddica Tomadora de Servi\xe7os prestados mediante cess\xe3o de m\xe3o de obra, exceto contratante de cooperativa, nos termos da lei 8.212/1991'), (b'5', '05 - Pessoa Jur\xeddica Tomadora de Servi\xe7os prestados por cooperados por interm\xe9dio de cooperativa de trabalho, exceto aqueles prestados a entidade beneficente/isenta'), (b'6', '06 - Entidade beneficente/isenta Tomadora de Servi\xe7os prestados por cooperados por interm\xe9dio de cooperativa de trabalho'), (b'7', '07 - Pessoa F\xedsica tomadora de Servi\xe7os prestados por Cooperados por interm\xe9dio de Cooperativa de Trabalho'), (b'8', '08 - Operador Portu\xe1rio tomador de servi\xe7os de trabalhadores avulsos'), (b'9', '09 - Contratante de trabalhadores avulsos n\xe3o portu\xe1rios por interm\xe9dio de Sindicato'), (b'90', '90 - Atividades desenvolvidas no exterior por trabalhador vinculado ao Regime Geral de Previd\xeancia Social (expatriados)'), (b'91', '91 - Atividades desenvolvidas por trabalhador estrangeiro vinculado a Regime de Previd\xeancia Social Estrangeiro')])),
                ('tpinsc', models.IntegerField(blank=True, null=True, choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)')])),
                ('nrinsc', models.CharField(max_length=15, null=True, blank=True)),
                ('fpas', models.IntegerField()),
                ('codtercs', models.CharField(max_length=4)),
                ('codtercssusp', models.CharField(max_length=4, null=True, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1020alteracao_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1020alteracao_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1020_evttablotacao', models.OneToOneField(related_name='s1020alteracao_s1020_evttablotacao', to='esocial.s1020evtTabLotacao')),
            ],
            options={
                'ordering': ['s1020_evttablotacao', 'codlotacao', 'inivalid', 'fimvalid', 'tplotacao', 'tpinsc', 'nrinsc', 'fpas', 'codtercs', 'codtercssusp'],
                'db_table': 's1020_alteracao',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1020alteracaoinfoEmprParcial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpinsccontrat', models.IntegerField(choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)')])),
                ('nrinsccontrat', models.CharField(max_length=14)),
                ('tpinscprop', models.IntegerField(choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)')])),
                ('nrinscprop', models.CharField(max_length=14)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1020alteracaoinfoemprparcial_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1020alteracaoinfoemprparcial_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1020_alteracao', models.OneToOneField(related_name='s1020alteracaoinfoemprparcial_s1020_alteracao', to='s1020.s1020alteracao')),
            ],
            options={
                'ordering': ['s1020_alteracao', 'tpinsccontrat', 'nrinsccontrat', 'tpinscprop', 'nrinscprop'],
                'db_table': 's1020_alteracao_infoemprparcial',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1020alteracaoinfoProcJudTerceiros',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1020alteracaoinfoprocjudterceiros_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1020alteracaoinfoprocjudterceiros_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1020_alteracao', models.OneToOneField(related_name='s1020alteracaoinfoprocjudterceiros_s1020_alteracao', to='s1020.s1020alteracao')),
            ],
            options={
                'ordering': ['s1020_alteracao'],
                'db_table': 's1020_alteracao_infoprocjudterceiros',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1020alteracaonovaValidade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inivalid', models.CharField(max_length=7, choices=[(b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('fimvalid', models.CharField(blank=True, max_length=7, null=True, choices=[(b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1020alteracaonovavalidade_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1020alteracaonovavalidade_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1020_alteracao', models.OneToOneField(related_name='s1020alteracaonovavalidade_s1020_alteracao', to='s1020.s1020alteracao')),
            ],
            options={
                'ordering': ['s1020_alteracao', 'inivalid', 'fimvalid'],
                'db_table': 's1020_alteracao_novavalidade',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1020alteracaoprocJudTerceiro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codterc', models.CharField(max_length=4)),
                ('nrprocjud', models.CharField(max_length=20)),
                ('codsusp', models.IntegerField()),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1020alteracaoprocjudterceiro_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1020alteracaoprocjudterceiro_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1020_alteracao_infoprocjudterceiros', models.ForeignKey(related_name='s1020alteracaoprocjudterceiro_s1020_alteracao_infoprocjudterceiros', to='s1020.s1020alteracaoinfoProcJudTerceiros')),
            ],
            options={
                'ordering': ['s1020_alteracao_infoprocjudterceiros', 'codterc', 'nrprocjud', 'codsusp'],
                'db_table': 's1020_alteracao_procjudterceiro',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1020exclusao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codlotacao', models.CharField(max_length=30)),
                ('inivalid', models.CharField(max_length=7, choices=[(b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('fimvalid', models.CharField(blank=True, max_length=7, null=True, choices=[(b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1020exclusao_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1020exclusao_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1020_evttablotacao', models.OneToOneField(related_name='s1020exclusao_s1020_evttablotacao', to='esocial.s1020evtTabLotacao')),
            ],
            options={
                'ordering': ['s1020_evttablotacao', 'codlotacao', 'inivalid', 'fimvalid'],
                'db_table': 's1020_exclusao',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1020inclusao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codlotacao', models.CharField(max_length=30)),
                ('inivalid', models.CharField(max_length=7, choices=[(b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('fimvalid', models.CharField(blank=True, max_length=7, null=True, choices=[(b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('tplotacao', models.CharField(max_length=2, choices=[(b'1', '01 - Classifica\xe7\xe3o da atividade econ\xf4mica exercida pela Pessoa Jur\xeddica para fins de atribui\xe7\xe3o de c\xf3digo FPAS, inclusive obras de constru\xe7\xe3o civil pr\xf3pria, exceto: a) empreitada parcial ou sub-empreitada de obra de constru\xe7\xe3o civil (utilizar op\xe7\xe3o 02); b) (...)'), (b'10', '10 - Embarca\xe7\xe3o inscrita no Registro Especial Brasileiro - REB'), (b'2', '02 - Obra de Constru\xe7\xe3o Civil - Empreitada Parcial ou Sub- empreitada'), (b'21', '21 - Classifica\xe7\xe3o da atividade econ\xf4mica ou obra pr\xf3pria de constru\xe7\xe3o civil da Pessoa F\xedsica'), (b'24', '24 - Empregador Dom\xe9stico'), (b'3', '03 - Pessoa F\xedsica Tomadora de Servi\xe7os prestados mediante cess\xe3o de m\xe3o de obra, exceto contratante de cooperativa'), (b'4', '04 - Pessoa Jur\xeddica Tomadora de Servi\xe7os prestados mediante cess\xe3o de m\xe3o de obra, exceto contratante de cooperativa, nos termos da lei 8.212/1991'), (b'5', '05 - Pessoa Jur\xeddica Tomadora de Servi\xe7os prestados por cooperados por interm\xe9dio de cooperativa de trabalho, exceto aqueles prestados a entidade beneficente/isenta'), (b'6', '06 - Entidade beneficente/isenta Tomadora de Servi\xe7os prestados por cooperados por interm\xe9dio de cooperativa de trabalho'), (b'7', '07 - Pessoa F\xedsica tomadora de Servi\xe7os prestados por Cooperados por interm\xe9dio de Cooperativa de Trabalho'), (b'8', '08 - Operador Portu\xe1rio tomador de servi\xe7os de trabalhadores avulsos'), (b'9', '09 - Contratante de trabalhadores avulsos n\xe3o portu\xe1rios por interm\xe9dio de Sindicato'), (b'90', '90 - Atividades desenvolvidas no exterior por trabalhador vinculado ao Regime Geral de Previd\xeancia Social (expatriados)'), (b'91', '91 - Atividades desenvolvidas por trabalhador estrangeiro vinculado a Regime de Previd\xeancia Social Estrangeiro')])),
                ('tpinsc', models.IntegerField(blank=True, null=True, choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)')])),
                ('nrinsc', models.CharField(max_length=15, null=True, blank=True)),
                ('fpas', models.IntegerField()),
                ('codtercs', models.CharField(max_length=4)),
                ('codtercssusp', models.CharField(max_length=4, null=True, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1020inclusao_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1020inclusao_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1020_evttablotacao', models.OneToOneField(related_name='s1020inclusao_s1020_evttablotacao', to='esocial.s1020evtTabLotacao')),
            ],
            options={
                'ordering': ['s1020_evttablotacao', 'codlotacao', 'inivalid', 'fimvalid', 'tplotacao', 'tpinsc', 'nrinsc', 'fpas', 'codtercs', 'codtercssusp'],
                'db_table': 's1020_inclusao',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1020inclusaoinfoEmprParcial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpinsccontrat', models.IntegerField(choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)')])),
                ('nrinsccontrat', models.CharField(max_length=14)),
                ('tpinscprop', models.IntegerField(choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)')])),
                ('nrinscprop', models.CharField(max_length=14)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1020inclusaoinfoemprparcial_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1020inclusaoinfoemprparcial_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1020_inclusao', models.OneToOneField(related_name='s1020inclusaoinfoemprparcial_s1020_inclusao', to='s1020.s1020inclusao')),
            ],
            options={
                'ordering': ['s1020_inclusao', 'tpinsccontrat', 'nrinsccontrat', 'tpinscprop', 'nrinscprop'],
                'db_table': 's1020_inclusao_infoemprparcial',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1020inclusaoinfoProcJudTerceiros',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1020inclusaoinfoprocjudterceiros_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1020inclusaoinfoprocjudterceiros_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1020_inclusao', models.OneToOneField(related_name='s1020inclusaoinfoprocjudterceiros_s1020_inclusao', to='s1020.s1020inclusao')),
            ],
            options={
                'ordering': ['s1020_inclusao'],
                'db_table': 's1020_inclusao_infoprocjudterceiros',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1020inclusaoprocJudTerceiro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codterc', models.CharField(max_length=4)),
                ('nrprocjud', models.CharField(max_length=20)),
                ('codsusp', models.IntegerField()),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1020inclusaoprocjudterceiro_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1020inclusaoprocjudterceiro_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1020_inclusao_infoprocjudterceiros', models.ForeignKey(related_name='s1020inclusaoprocjudterceiro_s1020_inclusao_infoprocjudterceiros', to='s1020.s1020inclusaoinfoProcJudTerceiros')),
            ],
            options={
                'ordering': ['s1020_inclusao_infoprocjudterceiros', 'codterc', 'nrprocjud', 'codsusp'],
                'db_table': 's1020_inclusao_procjudterceiro',
                'managed': True,
            },
        ),
    ]
