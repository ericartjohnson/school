from tastypie.resources import ModelResource
# from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.authorization import Authorization
from tastypie import fields
from classroom.models import *


class TeacherResource(ModelResource):
    class Meta:
        queryset = Teacher.objects.all()
        authorization = Authorization()

    def determine_format(self, request):
        return "application/json"


class StudentResource(ModelResource):
    class Meta:
        queryset = Student.objects.all()
        ordering = ["name", "id"]
        filtering = {
            "name": ('exact'),
        }
        authorization = Authorization()

    def determine_format(self, request):
        return "application/json"


class ClassResource(ModelResource):
    teacher = fields.ForeignKey(TeacherResource, 'teacher', full=True)
    students = fields.ManyToManyField(StudentResource, 'students', full=True)

    class Meta:
        queryset = Class.objects.all()
        authorization = Authorization()

    def determine_format(self, request):
        return "application/json"
