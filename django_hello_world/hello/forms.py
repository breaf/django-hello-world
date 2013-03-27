from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.models import User
from django.forms.extras import SelectDateWidget
from .models import UserProfile


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('date_of_birth', 'jabber', 'skype', 'bio', 'contacts', 'photo')
        widgets = {'date_of_birth': AdminDateWidget()}