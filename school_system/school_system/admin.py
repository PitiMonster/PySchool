from django.contrib import admin

from .models import Teacher, Student, SchoolClass, Subject, Grade


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject')
    search_fields = ['user']
    ordering = ['user']

class SchoolClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher')
    search_fields = ['name', 'teacher']
    ordering = ['name']

class GradeAdmin(admin.ModelAdmin):
    list_display = ('grade', 'subject', 'student', 'teacher')
    search_fields = ['student', 'subject', 'teacher']
    ordering = ['student']

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student)
admin.site.register(SchoolClass, SchoolClassAdmin)
admin.site.register(Subject)
admin.site.register(Grade, GradeAdmin)

# Register your models here.
