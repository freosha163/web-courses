from rest_framework import serializers
from .models import Teacher, Course, Webinar


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'position', 'experience', 'email', 'webinar', 'course']


class WebinarSerializer(serializers.ModelSerializer):
    teacher_webinar = serializers.PrimaryKeyRelatedField(many=True, required=True, queryset=Teacher.objects.all())

    class Meta:
        model = Webinar
        fields = ['id', 'title', 'description', 'start_date', 'duration', 'status', 'subject', 'teacher_webinar']


class CourseSerializer(serializers.ModelSerializer):
    teacher_course = serializers.PrimaryKeyRelatedField(many=True, required=True, queryset=Teacher.objects.all())

    class Meta:
        model = Course
        fields = ['id', 'description', 'start_date', 'end_date', 'subject', 'teacher_course']
