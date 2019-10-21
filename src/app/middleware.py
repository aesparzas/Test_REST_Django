import json
import logging

from django.utils import timezone
from django.utils.decorators import decorator_from_middleware

log = logging.getLogger('request')


class RequestLogMiddleware(object):
    def process_request(self, request):
        request.start_time = timezone.now()

    def process_response(self, request, response):

        if response['content-type'] == 'application/json':
            if getattr(response, 'streaming', False):
                response_body = '<<<Streaming>>>'
            else:
                response_body = response.content
        else:
            response_body = '<<<Not JSON>>>'

        log_data = {
            'user': request.user.pk,

            'remote_address': request.META['REMOTE_ADDR'],

            'request_method': request.method,
            'request_path': request.get_full_path(),
            'request_body': request.body,

            'response_status': response.status_code,
            'response_body': response_body,

            'run_time': timezone.now() - request.start_time,
        }

        log.info(log_data)

        return response


class RequestLogViewMixin(object):
    """
    Adds RequestLogMiddleware to any Django View by overriding as_view.
    """

    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super(RequestLogViewMixin, cls).as_view(*args, **kwargs)
        view = decorator_from_middleware(RequestLogMiddleware)(view)
        return view