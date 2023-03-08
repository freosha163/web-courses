from django.shortcuts import render
from .models import Teacher, Webinar, Course
from rest_framework import generics, viewsets
from .serializers import TeacherSerializer, WebinarSerializer, CourseSerializer
from rest_framework.response import Response


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class WebinarViewSet(viewsets.ModelViewSet):
    queryset = Webinar.objects.all()
    serializer_class = WebinarSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
