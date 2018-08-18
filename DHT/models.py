# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class DHTModel(models.Model):

    date_time = models.DateTimeField()
    humid = models.FloatField()
    temp = models.FloatField()
