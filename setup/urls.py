from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from school.views import (
    CourseViewSet,
    EnrollmentCourseList,
    EnrollmentStudentList,
    EnrollmentViewSet,
    StudentViewSet,
)

router = routers.DefaultRouter()
router.register('students', StudentViewSet, basename='students')
router.register('courses', CourseViewSet, basename='courses')
router.register('enrollments', EnrollmentViewSet, basename='enrollments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('students/<int:pk>/enrollments/', EnrollmentStudentList.as_view()),
    path('courses/<int:pk>/enrollments/', EnrollmentCourseList.as_view()),
]
