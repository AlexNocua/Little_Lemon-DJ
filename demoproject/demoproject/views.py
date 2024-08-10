from django.http import HttpResponse
from demoproject.demoproject.views import handler404


def handler404(request, exception):
    return HttpResponse('Page not found', status=404)

handler404 = 'demoproject.views.handler404'