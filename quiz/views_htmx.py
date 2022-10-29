from django.shortcuts import render, reverse
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#===========================================================================
from datetime import datetime, timedelta


#===========================================================================
from quiz.models import Quiz, Question,  Answer
from quiz.forms import  HtmxCreateQuizForm, HtmxCreateQuizForm,HtmxCreateQuestionForm, HtmxCreateAnswerForm 
from main.decorators import allowed_users
#===========================================================================

    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    # name = models.CharField(max_length=120)
    # topic = models.CharField(max_length=120)
    # number_of_questions = models.IntegerField()
    # time_to_finish = models.IntegerField(help_text="duration of the quiz in minutes")
    # required_score_to_pass = models.IntegerField(help_text="required score in %")
    # created = models.DateTimeField(auto_now_add=True)
    # expire_date = models.DateTimeField()
    # difficulty = models.CharField(max_length=6, choices=DIFF_CHOICES)



@login_required(login_url='login')

# #@allowed_users(permissions = [

#   ], require_all=True, redirect_to='login')

def quiz_creation_tree(request):
  quizzes = Quiz.objects.order_by("-created").filter(author=request.user)
  if request.GET.get("filter") and request.GET.get("filter") != "all":
        today = datetime.today()
        last_date = today - timedelta(days=1)
        
        filter =  request.GET.get("filter")
        
        if filter == "last_week":
          last_date = today - timedelta(days=7)
        if filter == "last_month":
          last_date = today - timedelta(days=30)
        if filter == "last_year":
          last_date = today - timedelta(days=365)

        quizzes = Quiz.objects.order_by("-created").filter(author=request.user, created__lte = today, created__gt= last_date)
        
  quiz_form = HtmxCreateQuizForm()
  context={
    "quizzes":quizzes,
    "quiz_form":quiz_form,
  }
  
  # if request.user.is_superuser:
  #   return render(request, "quiz/admin/quiz_creation_tree.html", context)
    
  return render(request, "quiz/register/create_quiz.html", context)



#===========================================================================

@login_required(login_url='login')
#@allowed_users(permissions = ["quiz.add_quiz"], redirect_to='login')
def htmx_quiz_create(request):
  form = HtmxCreateQuizForm()
  
  if request.method == "POST":
    form = HtmxCreateQuizForm(request.POST)#, initial={"author_id":request.user.id})

    if form.is_valid():
      
      quiz = Quiz.objects.create(
        author = request.user,
        name = form.cleaned_data["name"],
        topic = form.cleaned_data["topic"],
        number_of_questions = form.cleaned_data["number_of_questions"],
        time_to_finish = form.cleaned_data["time_to_finish"],
        required_score_to_pass = form.cleaned_data["required_score_to_pass"],
        expire_date = form.cleaned_data["expire_date"],
        difficulty = form.cleaned_data["difficulty"]
        
      )
      
      messages.success(request, 'Quiz is created successfully.')
      print('Quiz is created successfully.')
      form = HtmxCreateQuizForm()
  else:
    messages.info(request, 'You can create quiz new')
  
  context = {  
    "form":form,
    "show_messages":True,
    "title":f"Create Quiz",
    "action":f"/quizzes/htmx/create/",
  }
  return render(request, "components/forms.html", context)


@login_required(login_url='login')
#@allowed_users(permissions = ["quiz.change_quiz",], redirect_to='login')
def htmx_quiz_update(request, pk):
  quiz = Quiz.objects.get(id=pk)
  form = HtmxCreateQuizForm(instance=quiz)
  if request.method == "POST":
    form = HtmxCreateQuizForm(request.POST, instance=quiz)
    if form.is_valid():
      quiz = form.save()
      messages.success(request, 'Quiz is updated successfully.')
      print('Quiz is Updated successfully.')
      
      
  else:
    messages.info(request, 'You can update quiz new')
    
  context = {  
    "form":form,
    "show_messages":True,
    "title":f"Update Quiz",
    "action":f"/quizzes/htmx/{quiz.id}/update/",
  }
  return render(request, "components/forms.html", context)


@login_required(login_url='login')
#@allowed_users(permissions = ["quiz.delete_quiz",], redirect_to='login')
def htmx_quiz_delete(request, pk):
  quiz = Quiz.objects.get(id=pk)
  quiz.delete()
  return HttpResponse("")
#===========================================================================


#===========================================================================

@login_required(login_url='login')
#@allowed_users(permissions = ["quiz.add_question"], redirect_to='login')
def htmx_question_create(request, pk):
  quiz = Quiz.objects.get(id=pk)
  
  form = HtmxCreateQuestionForm()
  if request.method == "POST":
    form = HtmxCreateQuestionForm(request.POST)
    if form.is_valid():
      
      text= form.cleaned_data["text"]
      question = Question.objects.create(quiz=quiz, text=text)
      question.quiz = quiz
      question.save()
      messages.success(request, 'Question is created successfully.')
      print('Question is created successfully.')
      form = HtmxCreateQuestionForm()
  else:
    messages.info(request, 'You can create question new')
    
  print(quiz.question_set.all())
  context = {  
    "form":form,
    "show_messages":True,
    "title":f"Create Question for quiz {quiz}",
    "action":f"/quizzes/htmx/{quiz.id}/question/create/",
  }
  return render(request, "components/forms.html", context)


@login_required(login_url='login')
#@allowed_users(permissions = ["quiz.change_question"], redirect_to='login')
def htmx_question_update(request, pk):
  question = Question.objects.get(id=pk)
  quiz = Quiz.objects.get(question=question)
  
  form = HtmxCreateQuestionForm(instance=question)
  if request.method == "POST":
    form = HtmxCreateQuestionForm(request.POST, instance=question)
    if form.is_valid():
      question = form.save()
      messages.success(request, 'Question is updated successfully.')
      print('Question is Updated successfully.')
  else:
    messages.info(request, 'You can update question new')
    
  context = {  
    "form":form,
    "show_messages":True,
    "title":f"Update Question for quiz {quiz}",
    "action":f"/quizzes/htmx/question/{question.id}/update/",
  }
  return render(request, "components/forms.html", context)

@login_required(login_url='login')
#@allowed_users(permissions = ["quiz.delete_question"], redirect_to='login')
def htmx_question_delete(request, pk):
  question = Question.objects.get(id=pk)
  question.delete()
  return HttpResponse("")
#===========================================================================



#===========================================================================
@login_required(login_url='login')
#@allowed_users(permissions = ["quiz.add_answer"], redirect_to='login')
def htmx_answer_create(request, pk):
  question = Question.objects.get(id=pk)
  form = HtmxCreateAnswerForm()
  if request.method == "POST":
    form = HtmxCreateAnswerForm(request.POST)
    if form.is_valid():
      text= form.cleaned_data["text"]
      correct= form.cleaned_data["correct"]
      answer = Answer.objects.create(question=question, correct=correct, text=text)
      answer.question = question
      answer.save()
      messages.success(request, 'Answer is created successfully.')
      print('Answer is created successfully.')
      form = HtmxCreateAnswerForm()
  else:
    messages.info(request, 'You can create answer new')
    
  print(question.answer_set.all())
  context = {  
    "form":form,
    "show_messages":True,
    "title":f"Create Answer for question {question.text}",
    "action":f"/quizzes/htmx/question/{question.id}/answer/create/",
  }
  return render(request, "components/forms.html", context)




@login_required(login_url='login')
#@allowed_users(permissions = ["quiz.change_answer"], redirect_to='login')
def htmx_answer_update(request, pk):
  answer = Answer.objects.get(id=pk)
  question = Question.objects.get(answer=answer)
  form = HtmxCreateAnswerForm(instance=answer)
  if request.method == "POST":
    form = HtmxCreateAnswerForm(request.POST, instance=answer)
    if form.is_valid():
      answer = form.save()
      messages.success(request, 'Answer is updated successfully.')
      print('answer is Updated successfully.')
  else:
    messages.info(request, 'You can update answer new')
    
  context = {  
    "form":form,
    "show_messages":True,
    "title":f"Update Answer for question {question.text}",
    "action":f"/quizzes/htmx/answer/{answer.id}/update/",
  }
  return render(request, "components/forms.html", context)


@login_required(login_url='login')
#@allowed_users(permissions = ["quiz.delete_answer"], redirect_to='login')
def htmx_answer_delete(request, pk):
  answer = Answer.objects.get(id=pk)
  answer.delete()
  return HttpResponse("")
#===========================================================================



#===========================================================================

