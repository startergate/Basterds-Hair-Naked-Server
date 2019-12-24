from django.http import HttpResponse


# Create your views here.


def index(request):
    return HttpResponse("Hello World! Api updated at 2019-12-24 11:47")
