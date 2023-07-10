from django.shortcuts import render
from quiz.models import Question
#def quiz_view(request):
 #   questions = Question.objects.all()
  #  return render(request, 'quiz/quiz.html', {'questions': questions})
import random
def home_view(request):
    return render(request, 'home.html')

def quiz_view(request):
    questions = list(Question.objects.all()) # fetching our q's from database
    for question in questions:
        options = [question.option1, question.option2, question.option3, question.option4]
        random.shuffle(options)
        question.option1, question.option2, question.option3, question.option4 = options

    random.shuffle(questions)
# by using shufflle fun in random lib we able to  randomise all q's and choices.
    return render(request, 'quiz/quiz.html', {'questions': questions})

from .models import Question

def submit_quiz_view(request):
    if request.method == 'POST':
        # Retrieve the questions from the database
        questions = Question.objects.all()
      

        # Process the user's quiz submission and calculate the score
        score = 0
        for question in questions:
            selected_option = request.POST.get(str(question.id))
            if selected_option == question.correct_answer:
                score += 1
        score_1=((score)/5)*100
        score_2=5-score;

        # Render the results template
        return render(request, 'quiz/results.html', {'score': score, 'score_1': score_1,'score_2':score_2})
    return render(request, 'quiz/quiz.html', {'questions': questions})

