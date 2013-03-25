#-*- coding: utf-8 -*-
from .models import RequestRecord


class StoresRequestsMiddleware(object):

    def process_request(self, request):
        record = RequestRecord(content=request)
        if request.user.is_authenticated():
            record.user = request.user
        record.save()