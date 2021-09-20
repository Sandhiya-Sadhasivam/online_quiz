from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from quiz import models as QMODEL


# Create your views here.
@login_required()
def student_exam_view(request):
    courses = QMODEL.Course.objects.all()
    return render(request, 'quiz/quiz_level.html', {'courses': courses})


@login_required()
def take_exam_view(request, pk):
    course = QMODEL.Course.objects.get(id=pk)
    total_questions = QMODEL.Question.objects.all().filter(course=course).count()
    questions = QMODEL.Question.objects.all().filter(course=course)
    total_marks = 0
    for q in questions:
        total_marks = total_marks + q.marks

    return render(request, 'quiz/take-quiz.html',
                  {'course': course, 'total_questions': total_questions, 'total_marks': total_marks})
