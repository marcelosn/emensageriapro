# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s1020', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1020alteracao',
            name='tplotacao',
            field=models.CharField(max_length=2, choices=[(b'01', '01 - Classifica\xe7\xe3o da atividade econ\xf4mica exercida pela Pessoa Jur\xeddica para fins de atribui\xe7\xe3o de c\xf3digo FPAS, inclusive obras de constru\xe7\xe3o civil pr\xf3pria, exceto: a) empreitada parcial ou sub-empreitada de obra de constru\xe7\xe3o civil (utilizar op\xe7\xe3o 02); b) (...)'), (b'02', '02 - Obra de Constru\xe7\xe3o Civil - Empreitada Parcial ou Sub- empreitada'), (b'03', '03 - Pessoa F\xedsica Tomadora de Servi\xe7os prestados mediante cess\xe3o de m\xe3o de obra, exceto contratante de cooperativa'), (b'04', '04 - Pessoa Jur\xeddica Tomadora de Servi\xe7os prestados mediante cess\xe3o de m\xe3o de obra, exceto contratante de cooperativa, nos termos da lei 8.212/1991'), (b'05', '05 - Pessoa Jur\xeddica Tomadora de Servi\xe7os prestados por cooperados por interm\xe9dio de cooperativa de trabalho, exceto aqueles prestados a entidade beneficente/isenta'), (b'06', '06 - Entidade beneficente/isenta Tomadora de Servi\xe7os prestados por cooperados por interm\xe9dio de cooperativa de trabalho'), (b'07', '07 - Pessoa F\xedsica tomadora de Servi\xe7os prestados por Cooperados por interm\xe9dio de Cooperativa de Trabalho'), (b'08', '08 - Operador Portu\xe1rio tomador de servi\xe7os de trabalhadores avulsos'), (b'09', '09 - Contratante de trabalhadores avulsos n\xe3o portu\xe1rios por interm\xe9dio de Sindicato'), (b'10', '10 - Embarca\xe7\xe3o inscrita no Registro Especial Brasileiro - REB'), (b'21', '21 - Classifica\xe7\xe3o da atividade econ\xf4mica ou obra pr\xf3pria de constru\xe7\xe3o civil da Pessoa F\xedsica'), (b'24', '24 - Empregador Dom\xe9stico'), (b'90', '90 - Atividades desenvolvidas no exterior por trabalhador vinculado ao Regime Geral de Previd\xeancia Social (expatriados)'), (b'91', '91 - Atividades desenvolvidas por trabalhador estrangeiro vinculado a Regime de Previd\xeancia Social Estrangeiro')]),
        ),
        migrations.AlterField(
            model_name='s1020inclusao',
            name='tplotacao',
            field=models.CharField(max_length=2, choices=[(b'01', '01 - Classifica\xe7\xe3o da atividade econ\xf4mica exercida pela Pessoa Jur\xeddica para fins de atribui\xe7\xe3o de c\xf3digo FPAS, inclusive obras de constru\xe7\xe3o civil pr\xf3pria, exceto: a) empreitada parcial ou sub-empreitada de obra de constru\xe7\xe3o civil (utilizar op\xe7\xe3o 02); b) (...)'), (b'02', '02 - Obra de Constru\xe7\xe3o Civil - Empreitada Parcial ou Sub- empreitada'), (b'03', '03 - Pessoa F\xedsica Tomadora de Servi\xe7os prestados mediante cess\xe3o de m\xe3o de obra, exceto contratante de cooperativa'), (b'04', '04 - Pessoa Jur\xeddica Tomadora de Servi\xe7os prestados mediante cess\xe3o de m\xe3o de obra, exceto contratante de cooperativa, nos termos da lei 8.212/1991'), (b'05', '05 - Pessoa Jur\xeddica Tomadora de Servi\xe7os prestados por cooperados por interm\xe9dio de cooperativa de trabalho, exceto aqueles prestados a entidade beneficente/isenta'), (b'06', '06 - Entidade beneficente/isenta Tomadora de Servi\xe7os prestados por cooperados por interm\xe9dio de cooperativa de trabalho'), (b'07', '07 - Pessoa F\xedsica tomadora de Servi\xe7os prestados por Cooperados por interm\xe9dio de Cooperativa de Trabalho'), (b'08', '08 - Operador Portu\xe1rio tomador de servi\xe7os de trabalhadores avulsos'), (b'09', '09 - Contratante de trabalhadores avulsos n\xe3o portu\xe1rios por interm\xe9dio de Sindicato'), (b'10', '10 - Embarca\xe7\xe3o inscrita no Registro Especial Brasileiro - REB'), (b'21', '21 - Classifica\xe7\xe3o da atividade econ\xf4mica ou obra pr\xf3pria de constru\xe7\xe3o civil da Pessoa F\xedsica'), (b'24', '24 - Empregador Dom\xe9stico'), (b'90', '90 - Atividades desenvolvidas no exterior por trabalhador vinculado ao Regime Geral de Previd\xeancia Social (expatriados)'), (b'91', '91 - Atividades desenvolvidas por trabalhador estrangeiro vinculado a Regime de Previd\xeancia Social Estrangeiro')]),
        ),
    ]
