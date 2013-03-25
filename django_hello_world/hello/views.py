#-*- coding: utf-8 -*-
from annoying.decorators import render_to
from django.contrib.auth.models import User
from .forms import ProfileForm, UserForm
from .models import RequestRecord


@render_to('hello/home.html')
def home(request):
    users = User.objects.filter()
    if request.user.is_authenticated():
        if request.method == 'POST':
            user_form = UserForm(request.POST, instance=request.user)
            profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.get_profile())
            if user_form.is_valid():
                user_form.save()
            else:
                print user_form.errors
            if profile_form.is_valid():
                profile_form.save()
            else:
                print profile_form.errors
        else:
            user_form = UserForm(instance=request.user)
            profile_form = ProfileForm(instance=request.user.get_profile())
        return {'user_form': user_form, 'profile_form': profile_form}
    else:
        return {'users': users}


@render_to('hello/requests.html')
def requests(request):
    records = RequestRecord.objects.all()[:10]
    return {'records': records}
