from django.contrib import admin

from school.models import Course, Enrollment, Student


class StudentsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'email',
        'cpf',
        'birth_date',
        'phone',
    )
    list_display_links = (
        'id',
        'name',
    )
    list_per_page = 20
    search_fields = ('name',)


admin.site.register(Student, StudentsAdmin)


class CoursesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'code',
        'description',
    )
    list_display_links = (
        'id',
        'code',
    )
    search_fields = ('code',)


admin.site.register(Course, CoursesAdmin)


class EnrollmentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'period')
    list_display_links = ('id',)
    search_fields = ('student__name', 'course__code', 'period')


admin.site.register(Enrollment, EnrollmentsAdmin)
