from django.contrib import admin

from .models import Branch, Department, Subject, Section


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ( 'name' ,'location')
    search_fields = ('name',)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'branch',
        )
    list_filter = ('branch',)
    search_fields = ('name',)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'department',
        'teacher',
        )
    list_filter = ('department', 'teacher')
    search_fields = ('name',)


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'shift_time',
        'department',
        'level',
        'maximum_number_of_students',
    )
    list_filter = ('department',)
    search_fields = ('name',)
