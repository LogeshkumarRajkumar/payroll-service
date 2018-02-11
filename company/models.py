 # -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ..authentication.models import User


class Company(models.Model):
    name = models.CharField(max_length=100)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
