# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-10 20:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s2220', '0002_auto_20180912_1557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='s2220exmedocup',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2220exmedocup',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2220exmedocup',
            name='s2220_evtmonit',
        ),
        migrations.RemoveField(
            model_name='s2220toxicologico',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2220toxicologico',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2220toxicologico',
            name='s2220_evtmonit',
        ),
        migrations.AlterModelOptions(
            name='s2220exame',
            options={'managed': True, 'ordering': ['s2220_evtmonit', 'dtexm', 'procrealizado', 'obsproc', 'interprexm', 'ordexame', 'dtinimonit', 'dtfimmonit', 'indresult']},
        ),
        migrations.RemoveField(
            model_name='s2220exame',
            name='cpfresp',
        ),
        migrations.RemoveField(
            model_name='s2220exame',
            name='nisresp',
        ),
        migrations.RemoveField(
            model_name='s2220exame',
            name='nmresp',
        ),
        migrations.RemoveField(
            model_name='s2220exame',
            name='nrconsclasse',
        ),
        migrations.RemoveField(
            model_name='s2220exame',
            name='nrcrm',
        ),
        migrations.RemoveField(
            model_name='s2220exame',
            name='ufconsclasse',
        ),
        migrations.RemoveField(
            model_name='s2220exame',
            name='ufcrm',
        ),
        migrations.AlterField(
            model_name='s2220exame',
            name='obsproc',
            field=models.CharField(blank=True, max_length=999, null=True),
        ),
        migrations.AlterField(
            model_name='s2220exame',
            name='procrealizado',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='s2220exMedOcup',
        ),
        migrations.DeleteModel(
            name='s2220toxicologico',
        ),
    ]
