from django.contrib import admin

from blog.models import Blog, BlogFile, BlogImage, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'descriptions',
        'created',
        'updated',
    )
    list_filter = ('created', 'updated')
    search_fields = ('slug',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'title',
        'created',
        'updated',
        'published',
        'status',
    )
    list_filter = ('author', 'created', 'updated', 'published')

@admin.register(BlogImage)
class BlogImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image','blog', 'created')
    list_filter = ('created',)


@admin.register(BlogFile)
class BlogFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'file','blog', 'created')
    list_filter = ('created',)