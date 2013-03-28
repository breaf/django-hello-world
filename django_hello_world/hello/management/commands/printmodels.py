# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from hello.models import UserProfile, RequestRecord


class Command(BaseCommand):
    help = 'This command prints all project models and the count of objects in every model.'

    def handle(self, *args, **options):
        profile_model = UserProfile
        request_model = RequestRecord

        result = ""
        self.stdout.write('Models: %s \n' % result)
        self.stderr.write('error: \n')
        # raise CommandError(result)

