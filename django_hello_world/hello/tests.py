"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import os

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from django.conf import settings


class HttpTest(TestCase):

    def test_edit_contacts_login(self):
        self.assertTrue(self.client.login(username='admin', password='admin'))
        response = self.client.get(reverse('edit_contacts'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'form')

    def test_post(self):
        self.assertTrue(self.client.login(username='admin', password='admin'))
        response = self.client.post(reverse('edit_contacts'), {'first_name': 'test_name'})
        self.assertEqual(response.status_code, 302)
        user = User.objects.get(username='admin')
        self.assertEqual(user.first_name, 'test_name')

    def test_photo_upload(self):
        self.client.login(username='admin', password='admin')
        path = lambda *args: os.path.join(settings.PROJ_MODULE_ROOT, *args)
        p = path('hello', 'static', 'avatar.jpg')
        with open(p, 'rb') as photo:
            self.client.post(reverse('edit_contacts'), {'photo': photo})
        response = self.client.get(reverse('edit_contacts'))
        self.assertContains(response, 'id="avatar"')