from rest_framework import generics, viewsets

from school.models import Course, Enrollment, Student
from school.serializers import (
    CourseSerializer,
    EnrollmentCourseListSerializer,
    EnrollmentSerializer,
    EnrollmentStudentListSerializer,
    StudentSerializer,
)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()  # type: ignore
    serializer_class = StudentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()  # type: ignore
    serializer_class = CourseSerializer


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()  # type: ignore
    serializer_class = EnrollmentSerializer


class EnrollmentStudentList(generics.ListAPIView):
    def get_queryset(self):
        queryset = Enrollment.objects.filter(student_id=self.kwargs['pk'])  # type: ignore
        return queryset

    serializer_class = EnrollmentStudentListSerializer


class EnrollmentCourseList(generics.ListAPIView):
    def get_queryset(self):
        queryset = Enrollment.objects.filter(course_id=self.kwargs['pk'])  # type: ignore
        return queryset

    serializer_class = EnrollmentCourseListSerializer
