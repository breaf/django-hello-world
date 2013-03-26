"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from hello.models import RequestRecord


class HttpTest(TestCase):

    def test_home(self):
        c = Client()
        response = c.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '42 Coffee Cups Test Assignment')

    def test_records(self):
        before_count = RequestRecord.objects.count()
        c = Client()
        response = c.get(reverse('home'))
        after_count = RequestRecord.objects.count()
        self.assertGreater(after_count, before_count)

    def test_requests(self):
        c = Client()
        for i in range(10):
            response = c.get(reverse('home'))
        response = c.get(reverse('requests_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['records']), 10)
        self.assertEqual(response.context['records'][0].id, 1)