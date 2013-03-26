"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client


class HttpTest(TestCase):

    def test_home(self):
        c = Client()
        response = c.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '42 Coffee Cups Test Assignment')
        # Check for non empty name
        self.assertGreater(len(response.context['users'][0].first_name), 0)
        self.assertGreater(len(response.context['users'][0].last_name), 0)

    def test_ajax(self):
        self.assertTrue(self.client.login(username='admin', password='admin'))
        response = self.client.post(reverse('home'), HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
