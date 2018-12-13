# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-13 01:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s1040', '0003_auto_20181120_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1040alteracao',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='s1040alteracao',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s1040alteracao',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1040alteracaonovavalidade',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='s1040alteracaonovavalidade',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s1040alteracaonovavalidade',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1040exclusao',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='s1040exclusao',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s1040exclusao',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1040inclusao',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='s1040inclusao',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s1040inclusao',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
