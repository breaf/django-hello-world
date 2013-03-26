"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from settings import path


class HttpTest(TestCase):

    def test_home_login(self):
        self.assertTrue(self.client.login(username='admin', password='admin'))
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'form')

    def test_post(self):
        self.assertTrue(self.client.login(username='admin', password='admin'))
        response = self.client.post(reverse('home'), {'first_name': 'test_name'})
        self.assertEqual(response.status_code, 200)
        user = User.objects.get(username='admin')
        self.assertEqual(user.first_name, 'test_name')

    def test_photo_upload(self):
        self.client.login(username='admin', password='admin')
        p = path('hello', 'static', 'avatar.jpg')
        with open(p, 'rb') as photo:
            response = self.client.post(reverse('home'), {'photo': photo})
        self.assertContains(response, 'id="avatar"')