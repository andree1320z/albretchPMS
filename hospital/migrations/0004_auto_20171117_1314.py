# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 18:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_auto_20171117_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseuser',
            name='country',
            field=models.CharField(default='Perú', max_length=200),
        ),
        migrations.AlterField(
            model_name='staff',
            name='hospital',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hospital', to='hospital.Hospital'),
        ),
    ]
