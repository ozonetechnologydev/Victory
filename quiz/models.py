from email.policy import default
from django.db import models

import random

from accounts.models import User

class Quiz(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120)
    number_of_questions = models.IntegerField()
    time_to_finish = models.IntegerField(help_text="duration of the quiz in minutes")
    required_score_to_pass = models.IntegerField(help_text="required score in %")
    created = models.DateTimeField(auto_now_add=True)
    expire_date = models.DateTimeField()
    DIFF_CHOICES = (
        ('easy', 'easy'),
        ('medium', 'medium'),
        ('hard', 'hard'),
    )
    difficulty = models.CharField(max_length=6, choices=DIFF_CHOICES)

    def __str__(self):
        return f"{self.name}-{self.topic}"

    def get_num_questions(self):
        num_questions_exists = self.question_set.count()
        if num_questions_exists > self.number_of_questions:
            return self.number_of_questions
        else:
            return num_questions_exists
            

    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_questions]

    class Meta:
        verbose_name_plural = 'Quizzes'
        

class Question(models.Model):
    text = models.TextField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answer_set.all()

class Answer(models.Model):
    text = models.TextField()
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"
    
    
    
class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.FloatField(null=True, blank=True)
    duration = models.FloatField(null=True, blank=True)
    number_correct_answers = models.IntegerField(default=0)
    number_of_round = models.IntegerField(default=1)
    
    
    def is_pass(self):
        return self.score >= self.quiz.required_score_to_pass and self.duration <= self.quiz.time_to_finish
    
    
    def __str__(self):
        return f"question: {self.user}, answer: {self.quiz}, score: {self.score}"
    