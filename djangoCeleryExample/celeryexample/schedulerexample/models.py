# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CeleryTask(models.Model):
    """
    Model to store details about the task
    """
    task_name = models.CharField(max_length=128, blank=False, unique=True)
    task_description = models.CharField(max_length=256, blank=False)
    task_args = models.CharField(max_length=128,blank=False, default='[]')

    def __str__(self):
        """
        Returns human readable reprsentation of model
        """
        return "{}".format(self.task_name)
