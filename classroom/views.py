from django.http import HttpResponse
from classroom.models import Teacher


def index(request):
    teacher = Teacher.objects.get(name='Carrie')
    return HttpResponse('Hello {0}! '.format(teacher.name))


def newAction():
    return HttpResponse('Hi')
