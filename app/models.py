"""
Definition of models.
"""

from django.db import models


class Act(models.Model):
    act_title = models.CharField(max_length=200)
    act_link = models.CharField(max_length=200)
    
class Choice(models.Model):
    act = models.ForeignKey(Act)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
