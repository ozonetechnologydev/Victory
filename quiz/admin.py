from django.contrib import admin

# Register your models here.
from .models import Quiz, Question, Answer, Result


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'topic',
        'number_of_questions',
        'time_to_finish',
        'required_score_to_pass',
        'created',
        'expire_date',
        'difficulty',
    )
    search_fields = ('name',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'quiz', 'created')
    list_filter = ('quiz', 'created')


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'correct', 'question', 'created')
    list_filter = ('correct', 'question', 'created')


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz', 'score','duration')
    list_filter = ('user', 'quiz')
                                      