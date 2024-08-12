import re
from django.conf import settings
from django.shortcuts import redirect


class MediaAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith(settings.MEDIA_URL) or re.match(r'^/[^/]+/media/', request.path):
            if not request.user.is_authenticated:
                return redirect('users:login')
        response = self.get_response(request)
        return response
