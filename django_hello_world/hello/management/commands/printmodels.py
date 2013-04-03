# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.db.models import get_app, get_models


class Command(BaseCommand):
    help = 'This command prints all project models and the count of objects in every model.'

    def handle(self, *args, **options):
        models_dict = {}
        app = get_app('hello')
        for model in get_models(app):
            models_dict[model.__name__] = model.objects.count()
        self.stdout.write('%s \n' % str(models_dict))
        self.stderr.write('error: %s \n' % str(models_dict))
