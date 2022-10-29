from django.contrib import admin


from home.models import Review, Comment, Contact


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ( 'author', 'rating', 'created', 'body_text')
    list_filter = ('author', 'created')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ( 'author', 'body_text', 'created')
    list_filter = ('author', 'created',  'updated')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'message',
        'date_time',
    )
    list_filter = ('date_time',)

