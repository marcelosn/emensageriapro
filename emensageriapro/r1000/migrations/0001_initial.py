# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle_de_acesso', '0001_initial'),
        ('efdreinf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='r1000alteracao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inivalid', models.CharField(max_length=7, choices=[(b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('fimvalid', models.CharField(blank=True, max_length=7, null=True, choices=[(b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('classtrib', models.CharField(max_length=2)),
                ('indescrituracao', models.IntegerField(choices=[(0, '0 - Empresa N\xe3o obrigada \xe0 ECD'), (1, '1 - Empresa obrigada \xe0 ECD')])),
                ('inddesoneracao', models.IntegerField(choices=[(0, '0 - N\xe3o Aplic\xe1vel'), (1, '1 - Empresa enquadrada nos termos da Lei 12.546/2011 e altera\xe7\xf5es')])),
                ('indacordoisenmulta', models.IntegerField(choices=[(0, '0 - Sem acordo'), (1, '1 - Com acordo')])),
                ('indsitpj', models.IntegerField(blank=True, null=True, choices=[(0, '0 - Situa\xe7\xe3o Normal'), (1, '1 - Extin\xe7\xe3o'), (2, '2 - Fus\xe3o'), (3, '3 - Cis\xe3o'), (4, '4 - Incorpora\xe7\xe3o')])),
                ('nmctt', models.CharField(max_length=70)),
                ('cpfctt', models.CharField(max_length=11)),
                ('fonefixo', models.CharField(max_length=13, null=True, blank=True)),
                ('fonecel', models.CharField(max_length=13, null=True, blank=True)),
                ('email', models.CharField(max_length=60, null=True, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r1000alteracao_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r1000alteracao_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r1000_evtinfocontri', models.OneToOneField(related_name='r1000alteracao_r1000_evtinfocontri', to='efdreinf.r1000evtInfoContri')),
            ],
            options={
                'ordering': ['r1000_evtinfocontri', 'inivalid', 'fimvalid', 'classtrib', 'indescrituracao', 'inddesoneracao', 'indacordoisenmulta', 'indsitpj', 'nmctt', 'cpfctt', 'fonefixo', 'fonecel', 'email'],
                'db_table': 'r1000_alteracao',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r1000alteracaoinfoEFR',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ideefr', models.CharField(max_length=1, choices=[(b'N', 'N - N\xe3o \xe9 EFR'), (b'S', 'S - \xc9 EFR')])),
                ('cnpjefr', models.CharField(max_length=14, null=True, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r1000alteracaoinfoefr_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r1000alteracaoinfoefr_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r1000_alteracao', models.OneToOneField(related_name='r1000alteracaoinfoefr_r1000_alteracao', to='r1000.r1000alteracao')),
            ],
            options={
                'ordering': ['r1000_alteracao', 'ideefr', 'cnpjefr'],
                'db_table': 'r1000_alteracao_infoefr',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r1000alteracaonovaValidade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inivalid', models.CharField(max_length=7, choices=[(b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('fimvalid', models.CharField(blank=True, max_length=7, null=True, choices=[(b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r1000alteracaonovavalidade_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r1000alteracaonovavalidade_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r1000_alteracao', models.OneToOneField(related_name='r1000alteracaonovavalidade_r1000_alteracao', to='r1000.r1000alteracao')),
            ],
            options={
                'ordering': ['r1000_alteracao', 'inivalid', 'fimvalid'],
                'db_table': 'r1000_alteracao_novavalidade',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r1000alteracaosoftHouse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cnpjsofthouse', models.CharField(max_length=14)),
                ('nmrazao', models.CharField(max_length=115)),
                ('nmcont', models.CharField(max_length=70)),
                ('telefone', models.CharField(max_length=13, null=True, blank=True)),
                ('email', models.CharField(max_length=60, null=True, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r1000alteracaosofthouse_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r1000alteracaosofthouse_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r1000_alteracao', models.ForeignKey(related_name='r1000alteracaosofthouse_r1000_alteracao', to='r1000.r1000alteracao')),
            ],
            options={
                'ordering': ['r1000_alteracao', 'cnpjsofthouse', 'nmrazao', 'nmcont', 'telefone', 'email'],
                'db_table': 'r1000_alteracao_softhouse',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r1000exclusao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inivalid', models.CharField(max_length=7, choices=[(b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('fimvalid', models.CharField(blank=True, max_length=7, null=True, choices=[(b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r1000exclusao_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r1000exclusao_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r1000_evtinfocontri', models.OneToOneField(related_name='r1000exclusao_r1000_evtinfocontri', to='efdreinf.r1000evtInfoContri')),
            ],
            options={
                'ordering': ['r1000_evtinfocontri', 'inivalid', 'fimvalid'],
                'db_table': 'r1000_exclusao',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r1000inclusao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inivalid', models.CharField(max_length=7, choices=[(b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('fimvalid', models.CharField(blank=True, max_length=7, null=True, choices=[(b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('classtrib', models.CharField(max_length=2)),
                ('indescrituracao', models.IntegerField(choices=[(0, '0 - Empresa N\xe3o obrigada \xe0 ECD'), (1, '1 - Empresa obrigada \xe0 ECD')])),
                ('inddesoneracao', models.IntegerField(choices=[(0, '0 - N\xe3o Aplic\xe1vel'), (1, '1 - Empresa enquadrada nos termos da Lei 12.546/2011 e altera\xe7\xf5es')])),
                ('indacordoisenmulta', models.IntegerField(choices=[(0, '0 - Sem acordo'), (1, '1 - Com acordo')])),
                ('indsitpj', models.IntegerField(blank=True, null=True, choices=[(0, '0 - Situa\xe7\xe3o Normal'), (1, '1 - Extin\xe7\xe3o'), (2, '2 - Fus\xe3o'), (3, '3 - Cis\xe3o'), (4, '4 - Incorpora\xe7\xe3o')])),
                ('nmctt', models.CharField(max_length=70)),
                ('cpfctt', models.CharField(max_length=11)),
                ('fonefixo', models.CharField(max_length=13, null=True, blank=True)),
                ('fonecel', models.CharField(max_length=13, null=True, blank=True)),
                ('email', models.CharField(max_length=60, null=True, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r1000inclusao_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r1000inclusao_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r1000_evtinfocontri', models.OneToOneField(related_name='r1000inclusao_r1000_evtinfocontri', to='efdreinf.r1000evtInfoContri')),
            ],
            options={
                'ordering': ['r1000_evtinfocontri', 'inivalid', 'fimvalid', 'classtrib', 'indescrituracao', 'inddesoneracao', 'indacordoisenmulta', 'indsitpj', 'nmctt', 'cpfctt', 'fonefixo', 'fonecel', 'email'],
                'db_table': 'r1000_inclusao',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r1000inclusaoinfoEFR',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ideefr', models.CharField(max_length=1, choices=[(b'N', 'N - N\xe3o \xe9 EFR'), (b'S', 'S - \xc9 EFR')])),
                ('cnpjefr', models.CharField(max_length=14, null=True, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r1000inclusaoinfoefr_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r1000inclusaoinfoefr_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r1000_inclusao', models.OneToOneField(related_name='r1000inclusaoinfoefr_r1000_inclusao', to='r1000.r1000inclusao')),
            ],
            options={
                'ordering': ['r1000_inclusao', 'ideefr', 'cnpjefr'],
                'db_table': 'r1000_inclusao_infoefr',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r1000inclusaosoftHouse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cnpjsofthouse', models.CharField(max_length=14)),
                ('nmrazao', models.CharField(max_length=115)),
                ('nmcont', models.CharField(max_length=70)),
                ('telefone', models.CharField(max_length=13, null=True, blank=True)),
                ('email', models.CharField(max_length=60, null=True, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r1000inclusaosofthouse_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r1000inclusaosofthouse_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r1000_inclusao', models.ForeignKey(related_name='r1000inclusaosofthouse_r1000_inclusao', to='r1000.r1000inclusao')),
            ],
            options={
                'ordering': ['r1000_inclusao', 'cnpjsofthouse', 'nmrazao', 'nmcont', 'telefone', 'email'],
                'db_table': 'r1000_inclusao_softhouse',
                'managed': True,
            },
        ),
    ]
