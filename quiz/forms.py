


from tkinter import Widget
from turtle import width
from django import forms

from quiz.models import Answer, Question, Quiz
#===========================================================================


class HtmxCreateQuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['name','topic','number_of_questions','time_to_finish','required_score_to_pass','expire_date','difficulty']
        widgets = {
            'name': forms.TextInput(attrs={"class":"form-control","required":True, "placeholder":"Name",}),
            'topic': forms.TextInput(attrs={"class":"form-control","required":True, "placeholder":"Topic",}),
            'number_of_questions': forms.NumberInput(attrs={"class":"form-control","required":True,"type":"number","placeholder":"Number of questions"}),
            'required_score_to_pass': forms.NumberInput(attrs={"class":"form-control","required":True,"type":"number","placeholder":"Required score to pass"}),
            'time_to_finish': forms.NumberInput(attrs={"class":"form-control","required":True,"type":"number","placeholder":"Time to finish by minutes"}),
            'expire_date':forms.DateTimeInput(attrs={"class":"form-control", "placeholder":"Expire date", "type":"date"}),
            'difficulty':  forms.Select(attrs={'class': 'form-control single-select'}),
        
        }

class HtmxCreateQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={"class":"form-control summernoteEditor", "placeholder":"about body"}),   
        }
        
class HtmxCreateAnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text','correct']
        widgets = {
            'text': forms.Textarea(attrs={"class":"form-control summernoteEditor", "placeholder":"about body"}),   
            'correct': forms.CheckboxInput(attrs={"class":"inline-success"}),
        }
