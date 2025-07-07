from rest_framework import serializers

from school.models import Course, Enrollment, Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'


class EnrollmentStudentListSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='student.name')
    course = serializers.ReadOnlyField(source='course.description')
    period = serializers.SerializerMethodField()

    class Meta:
        model = Enrollment
        fields = ('student_name', 'course', 'period')

    def get_period(self, obj):
        return obj.get_period_display()


class EnrollmentCourseListSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='student.name')
    course_description = serializers.ReadOnlyField(source='course.description')

    class Meta:
        model = Enrollment
        fields = ('student_name', 'course_description')
