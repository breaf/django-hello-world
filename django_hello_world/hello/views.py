#-*- coding: utf-8 -*-
from annoying.decorators import render_to
from django.contrib.auth.models import User
from .models import RequestRecord


@render_to('hello/home.html')
def home(request):
    users = User.objects.filter()
    return {'users': users}


@render_to('hello/requests.html')
def requests(request):
    records = RequestRecord.objects.all()[:10]
    return {'records': records}
