from django.views.decorators.http import require_http_methods
from django.utils import simplejson as json
from django.http import HttpResponse
from smokealarm.models import Report


@require_http_methods(["POST"])
def report(request):
    kwargs = dict((k, v) for k, v in request.POST.iteritems())
    kwargs["owner"] = request.user if request.user.is_authenticated() else None
    kwargs["cookies"] = json.dumps(request.COOKIES)
    kwargs["meta"] = json.dumps(dict((k, request.META.get(k)) for k in [
        "HTTP_REFERER",
        "LANG",
        "HTTP_ACCEPT_CHARSET",
        "REMOTE_ADDR",
        "HTTP_USER_AGENT",
    ]))
    Report(**kwargs).save()
    return HttpResponse()
