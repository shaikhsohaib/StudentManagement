# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Parent(models.Model):
    gender_choice = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female')
        )

    email = models.EmailField(unique=True, null=False, blank=False)
    password = models.CharField(max_length=8, null=False, blank=False)
    firstname = models.TextField(max_length=20, null=False, blank=False)
    lastname = models.TextField(max_length=20, null=False, blank=False)
    gender = models.CharField(max_length=6, null=False, blank=False, choices=gender_choice)

    def __str__(self):
        return self.email





