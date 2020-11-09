# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Student(models.Model):
    gender_choice = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Other'),
    )
    firstname = models.TextField(max_length=15, null=False, blank=False)
    lastname = models.TextField(max_length=15, null=False, blank=False)
    email = models.EmailField(null=False, blank=False, unique=False)
    password = models.CharField(max_length=8, null=False, blank=False)
    gender = models.CharField(max_length=6, null=False, blank=False, choices=gender_choice)
    contact = models.IntegerField(max_length=10, null=False, blank=False, unique=True)

    def __str__(self):
        return self.email

