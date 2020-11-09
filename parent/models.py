# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import (AbstractUser, BaseUserManager)


# Create your models here.
class ParentManager(BaseUserManager):
    def create_user(self, firstname, lastname, email, gender, password=None):
        if not email:
            raise ValueError("Parent must have email address")

        parent = self.model(
            email=self.normalize_email(email),
            firstname=firstname,
            lastname=lastname,
            gender=gender
        )

        parent.set_password(password)
        parent.save(using=self._db)
        return parent

    def create_staff(self, firstname, lastname, email, gender, password):
        parent = self.create_user(
            email,
            firstname=firstname,
            lastname=lastname,
            gender=gender,
            password=password
        )

        parent.staff = True
        parent.save(using=self._db)
        return parent


class Parent(AbstractUser):
    gender_choice = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female')
        )
    firstname = models.TextField(max_length=20, null=False, blank=False)
    lastname = models.TextField(max_length=20, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    gender = models.TextField(max_length=6, choices=gender_choice, null=False, blank=False)

    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_active(self):
        return self.active

    parentobject = ParentManager()

