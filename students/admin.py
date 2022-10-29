from django.contrib import admin

from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'admission_date',
        'payment',
        'status',
    )
    list_filter = ('user', 'admission_date')