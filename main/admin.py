from django.contrib import admin

from .models import GeneralSetting, OfficeAddress, SocialNetwork, PhoneNumber, EmailAddress, CoreValue, Team, AboutUs, Image, File, Gallery


@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = (
        'site_name',
        'logo',
        'favicon',
        'created',
        'updated',
    )
    list_filter = ('created', 'updated')


@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')
    list_filter = ('created',)
    search_fields = ('name',)


@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ('number', 'created')
    list_filter = ('created',)


@admin.register(EmailAddress)
class EmailAddressAdmin(admin.ModelAdmin):
    list_display = ('email', 'created')
    list_filter = ('created',)


@admin.register(CoreValue)
class CoreValuesAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    list_filter = ('created',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'created')
    list_filter = ('created',)



@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    list_filter = ('created',)



@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image','created')
    list_filter = ('created',)


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('file','created')
    list_filter = ('created',)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    list_filter = ('created',)

@admin.register(OfficeAddress)
class OfficeAddressAdmin(admin.ModelAdmin):
    list_display = ('office', 'street', 'city', 'state')
