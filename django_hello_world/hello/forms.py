from django import forms
from hello.models import UserProfile


class ProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile