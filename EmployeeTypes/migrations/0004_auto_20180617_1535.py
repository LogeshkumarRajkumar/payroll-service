# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-06-17 15:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeTypes', '0003_employeetype_waged'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeetype',
            old_name='waged',
            new_name='salaried',
        ),
    ]