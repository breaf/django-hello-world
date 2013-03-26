"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.http import HttpRequest
from django.template import Template, RequestContext
from django.test import TestCase
from django.conf import settings


class HttpTest(TestCase):

    def test_home(self):
        context = RequestContext(HttpRequest())
        result = Template('{{ settings.DEBUG }}').render(context)
        self.assertEqual(result, str(settings.DEBUG))
