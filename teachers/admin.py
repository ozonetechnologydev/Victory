from django.contrib import admin

from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'joining_date',
        'profession',
        'salary',
    )
    list_filter = ('user', 'joining_date')