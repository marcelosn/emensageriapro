# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-10 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabelas', '0006_auto_20181110_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='esocialdesligamentosmotivos',
            name='data_termino',
            field=models.DateField(blank=True, null=True),
        ),
    ]
