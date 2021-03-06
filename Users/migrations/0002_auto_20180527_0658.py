# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-27 06:58
from __future__ import unicode_literals

import Common.Validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=20000, validators=[Common.Validators.validate_alpha_numeric], verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=20000, validators=[Common.Validators.validate_alpha_numeric], verbose_name='last name'),
        ),
    ]
