#-*- coding: utf-8 -*-
from django.contrib.contenttypes.models import ContentType


def logging_changes(sender, instance, created, **kwargs):
    from .models import LogRecord
    log_record = LogRecord(
        content_type=ContentType.objects.get_for_model(sender),
        object_id=instance.id,
        changes_type='crd' if created else 'edd'
    )
    log_record.save()


def logging_deletion(sender, instance, **kwargs):
    from .models import LogRecord
    log_record = LogRecord(
        content_type=ContentType.objects.get_for_model(sender),
        object_id=instance.id,
        changes_type='dld'
    )
    log_record.save()