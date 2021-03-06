# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-22 22:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controle_de_acesso', '0009_auto_20181120_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditoria',
            name='data_hora',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='auditoria',
            name='identidade',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='auditoria',
            name='operador',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='auditoria_operador', to='controle_de_acesso.Usuarios'),
        ),
        migrations.AlterField(
            model_name='auditoria',
            name='situacao_anterior',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='auditoria',
            name='situacao_posterior',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='auditoria',
            name='tabela',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='auditoria',
            name='tipo',
            field=models.IntegerField(blank=True, choices=[(1, 'Inclus\xe3o'), (2, 'Altera\xe7\xe3o'), (3, 'Exclus\xe3o')]),
        ),
    ]
