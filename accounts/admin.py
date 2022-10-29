from django.contrib import admin

from .models import User, Address, UserImage


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'first_name',
        'last_name',
        'username',
        'gender',
        'birth_date',
        'is_superuser',
        'is_active',
        'is_staff',
        'last_login',
        'date_joined',
        'bio',
        'id',
    )
    list_filter = (
        'last_login',
        'is_superuser',
        'is_staff',
        'is_active',
        'date_joined',
        'birth_date',
    )
    raw_id_fields = ('groups', 'user_permissions')


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'street', 'city', 'state')
    list_filter = ('user',)


@admin.register(UserImage)
class UserImageAdmin(admin.ModelAdmin):
    list_display = ('user', 'image', 'created', 'about', 'role')
    list_filter = ('user', 'created')
                                        