#-*- coding: utf-8 -*-
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from .signals import logging_changes, logging_deletion


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

post_save.connect(logging_changes, sender=UserProfile, dispatch_uid="unique_UserProfile_save_identifier")
post_delete.connect(logging_deletion, sender=UserProfile, dispatch_uid="unique_UserProfile_delete_identifier")

post_save.connect(logging_changes, sender=User, dispatch_uid="unique_User_save_identifier")
post_delete.connect(logging_deletion, sender=User, dispatch_uid="unique_User_delete_identifier")


class RequestRecord(models.Model):
    user = models.ForeignKey(User, related_name="requests", null=True, blank=True)
    content = models.TextField("Request content")
    added_at = models.DateTimeField("Added at", auto_now_add=True)
    priority = models.PositiveIntegerField("Priority", default=0)

    class Meta:
        ordering = ('-priority', 'added_at')

post_save.connect(logging_changes, sender=RequestRecord, dispatch_uid="unique_RequestRecord_save_identifier")
post_delete.connect(logging_deletion, sender=RequestRecord, dispatch_uid="unique_RequestRecord_delete_identifier")


class LogRecord(models.Model):
    TYPE_CHOICES = (('crd', 'Created'),
                    ('edd', 'Edited'),
                    ('dld', 'Deleted'))

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    changes_type = models.CharField('Type of changes', max_length=3, choices=TYPE_CHOICES)
    added_at = models.DateTimeField("Added at", auto_now_add=True)

    def __unicode__(self):
        return "%s [%s] %s at %s" % (self.content_type, self.object_id, self.get_changes_type_display(), self.added_at)

