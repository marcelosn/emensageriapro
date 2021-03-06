# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-13 02:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s2241', '0004_auto_20181120_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s2241altaposentesp',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='s2241altaposentesp',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s2241altaposentesp',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2241altaposentespfatrisco',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='s2241altaposentespfatrisco',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s2241altaposentespfatrisco',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2241altaposentespinfoamb',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='s2241altaposentespinfoamb',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s2241altaposentespinfoamb',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2241altinsalperic',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='s2241altinsalperic',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s2241altinsalperic',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2241altinsalpericfatrisco',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='s2241altinsalpericfatrisco',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s2241altinsalpericfatrisco',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2241altinsalpericinfoamb',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='s2241altinsalpericinfoamb',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s2241altinsalpericinfoamb',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2241fimaposentesp',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='s2241fimaposentesp',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s2241fimaposentesp',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2241fimaposentespinfoamb',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='s2241fimaposentespinfoamb',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s2241fimaposentespinfoamb',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2241fiminsalperic',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='s2241fiminsalperic',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s2241fiminsalperic',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2241fiminsalpericinfoamb',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='s2241fiminsalpericinfoamb',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s2241fiminsalpericinfoamb',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2241iniaposentesp',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='s2241iniaposentesp',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s2241iniaposentesp',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2241iniaposentespfatrisco',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='s2241iniaposentespfatrisco',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s2241iniaposentespfatrisco',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2241iniaposentespinfoamb',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='s2241iniaposentespinfoamb',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s2241iniaposentespinfoamb',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2241iniinsalperic',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='s2241iniinsalperic',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s2241iniinsalperic',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2241iniinsalpericfatrisco',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='s2241iniinsalpericfatrisco',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s2241iniinsalpericfatrisco',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2241iniinsalpericinfoamb',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='s2241iniinsalpericinfoamb',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s2241iniinsalpericinfoamb',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
