# -*- coding: utf-8 -*-
from django import template
from django.core.urlresolvers import reverse


register = template.Library()


@register.simple_tag
def edit_link(obj):
    model = obj.__class__
    app_label = model._meta.app_label
    model_name = model.__name__.lower()
    edit_view_name = 'admin:%s_%s_change' % (app_label, model_name)
    edit_url = reverse(edit_view_name, args=[obj.pk])
    return '<a href="%s">admin</a>' % edit_url
