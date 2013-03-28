"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import os
import datetime

from django.core.urlresolvers import reverse
from django.http import HttpRequest
from django.template import RequestContext, Template
from django.test import TestCase
from django.contrib.auth.models import User
from django.conf import settings
from .models import UserProfile


class HttpTest(TestCase):

    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '42 Coffee Cups Test Assignment')
        # Check for non empty name
        self.assertGreater(len(response.context['user'].first_name), 0)
        self.assertGreater(len(response.context['user'].last_name), 0)

    def test_ajax(self):
        self.assertTrue(self.client.login(username='admin', password='admin'))
        response = self.client.post(reverse('edit_contacts'), HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'success')

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

        photo = User.objects.get(username='admin').userprofile.photo
        photo.delete()

    def test_tag(self):
        user = User.objects.get(username='admin')
        context = RequestContext(HttpRequest())
        context['user'] = user
        result = Template('{% load edit_tag %}{% edit_link user %}').render(context)
        self.assertEqual(result, '<a href="/admin/auth/user/%s/">admin</a>' % user.id)

    def test_bash_script(self):
        os.popen("bash command_execute")
        filename = '%s.dat' % datetime.date.today()
        path = lambda *args: os.path.join(settings.PROJ_MODULE_ROOT, *args)
        f = path(filename)
        with open(f, 'r') as log_file:
            contents = log_file.read()
            models_dict = eval(contents)
        self.assertTrue(models_dict['UserProfile'] == UserProfile.objects.count())
        os.remove(f)
