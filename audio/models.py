# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class AbnormalityModel(models.Model):

    date_time = models.DateTimeField()


class FileModel(models.Model):

    file = models.FileField(blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_checked = models.BooleanField(default=False)