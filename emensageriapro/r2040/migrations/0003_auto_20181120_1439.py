# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-20 14:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('r2040', '0002_auto_20181118_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='r2040infoproc',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='r2040infoproc',
            name='nrproc',
            field=models.CharField(max_length=21),
        ),
        migrations.AlterField(
            model_name='r2040infoproc',
            name='r2040_recursosrep',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='r2040infoproc_r2040_recursosrep', to='r2040.r2040recursosRep'),
        ),
        migrations.AlterField(
            model_name='r2040infoproc',
            name='tpproc',
            field=models.IntegerField(choices=[(1, '1 - Administrativo'), (2, '2 - Judicial')]),
        ),
        migrations.AlterField(
            model_name='r2040infoproc',
            name='vlrnret',
            field=models.DecimalField(decimal_places=2, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='r2040inforecurso',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='r2040inforecurso',
            name='descrecurso',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='r2040inforecurso',
            name='r2040_recursosrep',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='r2040inforecurso_r2040_recursosrep', to='r2040.r2040recursosRep'),
        ),
        migrations.AlterField(
            model_name='r2040inforecurso',
            name='tprepasse',
            field=models.IntegerField(choices=[(1, '1 - Patroc\xednio'), (2, '2 - Licenciamento de marcas e s\xedmbolos'), (3, '3 - Publicidade'), (4, '4 - Propaganda'), (5, '5 - Transmiss\xe3o de espet\xe1culos')]),
        ),
        migrations.AlterField(
            model_name='r2040inforecurso',
            name='vlrbruto',
            field=models.DecimalField(decimal_places=2, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='r2040inforecurso',
            name='vlrretapur',
            field=models.DecimalField(decimal_places=2, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='r2040recursosrep',
            name='cnpjassocdesp',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='r2040recursosrep',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='r2040recursosrep',
            name='r2040_evtassocdesprep',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='r2040recursosrep_r2040_evtassocdesprep', to='efdreinf.r2040evtAssocDespRep'),
        ),
        migrations.AlterField(
            model_name='r2040recursosrep',
            name='vlrtotalrep',
            field=models.DecimalField(decimal_places=2, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='r2040recursosrep',
            name='vlrtotalret',
            field=models.DecimalField(decimal_places=2, max_digits=15, max_length=14),
        ),
    ]