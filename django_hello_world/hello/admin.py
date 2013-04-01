#-*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile, RequestRecord, LogRecord


admin.site.unregister(User)


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    extra = 0


class UserProfileAdmin(UserAdmin):
    inlines = [UserProfileInline, ]


class RequestRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'added_at')


admin.site.register(User, UserProfileAdmin)
admin.site.register(RequestRecord, RequestRecordAdmin)
admin.site.register(LogRecord)

