from django.shortcuts import render_to_response
from django.views.decorators.csrf import ensure_csrf_cookie
from django.template import RequestContext


@ensure_csrf_cookie
def index(request):
    return render_to_response('client/index.html', {}, context_instance=RequestContext(request))
