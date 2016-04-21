# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 11:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tueti', '0002_tuetiuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tuet',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tueti.TuetiUser'),
        ),
        migrations.AlterField(
            model_name='tuet',
            name='response_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tueti.Tuet'),
        ),
    ]
