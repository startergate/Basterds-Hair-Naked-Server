from django.http import HttpResponse


# Create your views here.


def index(request):
    return HttpResponse("Hello World! Api updated at 2019-12-25 20:20")
