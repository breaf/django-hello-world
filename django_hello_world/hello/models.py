#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField("Date of birth", null=True, blank=True)
    jabber = models.CharField("Jabber", max_length=100, null=True, blank=True)
    skype = models.CharField("Skype", max_length=100, null=True, blank=True)
    bio = models.TextField("Bio", null=True, blank=True)
    contacts = models.TextField("Other contacts", null=True, blank=True)

    class Meta:
        verbose_name = u"profile"
