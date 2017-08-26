from django.http import Http404, HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello World")

def current_date_time(request):
    current = datetime.datetime.now()
    html = "<head><body>Current time %s.</body></head>" % current
    return HttpResponse(html)

def add(request, one, two):
    try:
        one = int(one)
        two = int(two)
        #assert False
    except ValueError:
        raise Http404()
    a = one + two
    return HttpResponse(str(a))
