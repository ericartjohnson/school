from django.http import HttpResponse
from classroom.models import Class
from classroom.models import Teacher
# from classroom.models import Student
# from django.db.models import Q
from django.core import serializers
from cleanjson.util import jsonResponse
from django.shortcuts import get_object_or_404


def get(request, pk):
    if pk is None:
        classes = Class.objects.all()
        data = serializers.serialize("json", classes, indent=4, relations=('teacher', 'students'))
    else:
        thisClass = get_object_or_404(Class, pk=pk)
        data = serializers.serialize("json", [thisClass], indent=4, relations=('teacher', 'students'))
    return jsonResponse(request, data)


def post(request, pk):
    if pk is None:
        # TODO validate post data before attempting to create new entry
        newClass = Class(name=request.POST["name"])
        newClass.save()
        data = serializers.serialize("json", [newClass], indent=4, relations=('teacher', 'students'))
        return jsonResponse(request, data)
    else:
        # return 403 error. Cannot post to a single classroom (not a collection)
        print ".."

    return HttpResponse("POST")


def put(request, pk):
    print request
    if pk is None:
        # return 403 error. Cannot replace the whole collection willy nilly.
        print ".."
    else:
        thisClass = get_object_or_404(Class, pk=pk)
        thisClass.name = request.POST["name"]
        thisClass.teacher = Teacher.objects.get(pk=request.POST["teacher"])
        #TODO build in Q objects for adding students correctly
        data = serializers.serialize("json", [thisClass], indent=4, relations=('teacher', 'students'))
        return jsonResponse(request, data)

    return HttpResponse("PUT")


def delete(request, pk):
    return HttpResponse("DELETE")


def index(request, pk=None):
    if request.method == "GET":
        return get(request, pk)
    elif request.method == "POST":
        return post(request, pk)
    elif request.method == "PUT":
        return put(request, pk)
    elif request.method == "DELETE":
        return delete(request, pk)
