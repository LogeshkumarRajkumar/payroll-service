# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-10-14 18:49
from __future__ import unicode_literals

import Common.Validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Employees', '0005_auto_20181014_1849'),
        ('Clients', '0001_initial'),
        ('Companies', '0002_auto_20180610_1242'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=200, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, validators=[Common.Validators.validate_alpha_numeric])),
                ('salary', models.FloatField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clients.Client')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Companies.Company')),
                ('employeeType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employees.EmployeeType')),
            ],
        ),
    ]
