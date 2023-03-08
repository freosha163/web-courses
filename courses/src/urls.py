from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeacherViewSet, WebinarViewSet, CourseViewSet

app_name = 'src'

router_v1 = DefaultRouter()
router_v1.register(r'teacher', TeacherViewSet, basename='teacher')
router_v1.register(r'webinar', WebinarViewSet, basename='webinar')
router_v1.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('api/v1/', include(router_v1.urls))
]
