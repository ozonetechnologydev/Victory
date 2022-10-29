from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse



from quiz.forms import HtmxCreateQuizForm

from quiz.models import Question, Quiz, Result

# Create your views here.


def quiz(request):
    quizzes = Quiz.objects.all()
    print(quizzes)
    complex = {
        "quizzes":quizzes,
    }
    return render(request, "quiz/public/quiz.html", complex)




def quizzes_list(request):
    quizzes = Quiz.objects.all()
    context ={
        "quizzes":quizzes,
    }
    return render(request, "quiz/public/quizzes_list.html",context)




def take_quizzes(request, pk):
    quiz = Quiz.objects.get(id=pk)
    questions = quiz.get_questions()
    if request.method == "POST":
        
        user_quiz_id = request.POST.get("quiz_id")
        user_questions = request.POST.getlist("users_questions")
        user_answers = request.POST.getlist("user_answers")
        quiz_duration = request.POST.get("quiz_duration")
        quiz_duration = round(float(quiz_duration), 2)

        
        if int(quiz.id) == int(user_quiz_id):
            quiz_questions = quiz.question_set.filter(id__in = user_questions)
            num_questions = quiz_questions.count()
            
            user_answers = list(filter(lambda x:  not x in ["none", None, 'null'], user_answers))
            num_correct_answers = quiz_questions.filter(answer__id__in = user_answers, answer__correct=True).count()

            score = (num_correct_answers/num_questions) * 100
        
            result, created = Result.objects.get_or_create(user = request.user, quiz=quiz)
   
            result.score = round(score, 2)
            result.duration = quiz_duration
            result.number_correct_answers = num_correct_answers
            result.number_of_round = result.number_of_round + 1
            
            print(result)
            result.save()
                                
            is_pass =result.is_pass()   
            number_of_round = result.number_of_round
            
            results = {
                "score":round(score, 2),
                "num_correct_answers":num_correct_answers,
                "is_pass":is_pass,
                "number_of_round": number_of_round,
            }            
            
            return JsonResponse(results)
    
    context = {
        "quiz":quiz,
        "questions":questions,
    }
    return render(request, "quiz/public/take_quizzes.html", context)

