from django.contrib import admin

from .models import Teacher, Student, SchoolClass


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject')
    search_fields = ['user']
    ordering = ['user']

class SchoolClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher')
    search_fields = ['name', 'teacher']
    ordering = ['name']

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student)
admin.site.register(SchoolClass, SchoolClassAdmin)


# Register your models here.
