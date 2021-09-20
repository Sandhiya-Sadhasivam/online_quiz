from django.urls import path

from quiz import views

app_name = "quiz"

urlpatterns = [
    path('list', views.student_exam_view, name='quiz-list'),
    path('take-quiz/<int:pk>', views.take_exam_view, name='take-quiz'),
    path('start-quiz/<int:pk>', views.start_exam_view, name='start-quiz'),
    path('calculate-marks', views.calculate_marks_view, name='calculate-marks'),
]
