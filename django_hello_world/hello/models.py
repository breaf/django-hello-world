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
    photo = models.ImageField("Photo", upload_to='photos', null=True, blank=True)

    class Meta:
        verbose_name = u"profile"


class RequestRecord(models.Model):
    user = models.ForeignKey(User, related_name="requests", null=True, blank=True)
    content = models.TextField("Request content")
    added_at = models.DateTimeField("Added at", auto_now_add=True)

