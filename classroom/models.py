from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher, null=True, blank=True)
    students = models.ManyToManyField(Student)

    def __unicode__(self):
        return self.name
