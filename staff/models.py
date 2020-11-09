# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import (AbstractUser)


class Staff(AbstractUser):
    contact = models.TextField(max_length=10, null=False, blank=True, unique=True)
    email = models.EmailField(null=False, blank=False, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
