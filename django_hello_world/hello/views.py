#-*- coding: utf-8 -*-
from annoying.decorators import render_to
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils import simplejson
from .forms import ProfileForm, UserForm
from .models import RequestRecord


@render_to('hello/home.html')
def home(request):
    try:
        user = User.objects.get(id=1)
    except User.DoesNotExist:
        return HttpResponse("Error. There is no any users in database.")

    return {'user': user}


@login_required
@render_to('hello/edit.html')
def edit_contacts(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.get_profile())
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            if request.is_ajax():
                return HttpResponse(simplejson.dumps({"success": True, }), content_type="application/json")
            else:
                return redirect('home')
        else:
            print user_form.errors
            print profile_form.errors
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.get_profile())
    return {'user_form': user_form, 'profile_form': profile_form}



@render_to('hello/requests.html')
def requests(request):
    records = RequestRecord.objects.all()[:10]
    return {'records': records}
