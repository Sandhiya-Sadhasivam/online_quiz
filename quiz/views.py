from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from accounts import models
from quiz import models as QMODEL


# Create your views here.
@login_required()
def student_exam_view(request):
    courses = QMODEL.Course.objects.all().filter(is_published= True)
    return render(request, 'quiz/quiz_level.html', {'courses': courses })


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


@login_required()
def start_exam_view(request, pk):
    course = QMODEL.Course.objects.get(id=pk)
    questions = QMODEL.Question.objects.all().filter(course=course)
    if request.method == 'POST':
        pass
    response = render(request, 'quiz/start-quiz.html', {'course': course, 'questions': questions})
    response.set_cookie('course_id', course.id)
    return response


@login_required()
def calculate_marks_view(request):
    if request.COOKIES.get('course_id') is not None:
        course_id = request.COOKIES.get('course_id')
        course = QMODEL.Course.objects.get(id=course_id)

        total_marks = 0
        questions = QMODEL.Question.objects.all().filter(course=course)
        for i in range(len(questions)):

            selected_ans = request.COOKIES.get(str(i + 1))
            actual_answer = questions[i].answer
            if selected_ans == actual_answer:
                total_marks = total_marks + questions[i].marks
        student = models.Student.objects.get(user_id=request.user.id)
        result = QMODEL.Result()
        result.marks = total_marks
        result.level = course
        result.student = student
        result.save()

        return redirect('quiz:view-result')


@login_required()
def view_result_view(request):
    courses = QMODEL.Course.objects.all().filter(is_published= True)
    return render(request, 'quiz/result.html', {'courses': courses})


@login_required()
def check_marks_view(request, pk):
    course = QMODEL.Course.objects.get(id=pk)
    student = models.Student.objects.get(user_id=request.user.id)
    results = QMODEL.Result.objects.all().filter(level=course).filter(student=student)
    return render(request, 'quiz/mark.html', {'results': results, 'course': course})


def view_leaderboard_view(request):
    courses = QMODEL.Course.objects.all().filter(is_published= True)
    return render(request, 'quiz/leaderboad-list.html', {'courses': courses})

def check_leaderboard_score_view(request, pk):
    course = QMODEL.Course.objects.get(id=pk)
    top_quiz_profiles = QMODEL.Result.objects.order_by('-marks').filter(level=course)
    total_count = top_quiz_profiles.count()
    context = {
        'top_quiz_profiles': top_quiz_profiles,
        'total_count': total_count,
    }
    return render(request, 'quiz/leaderboard.html', context=context)
