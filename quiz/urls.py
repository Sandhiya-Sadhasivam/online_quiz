from django.urls import path

from quiz import views

app_name = "quiz"

urlpatterns = [
    path('list', views.student_exam_view, name='quiz-list'),
    path('take-quiz/<int:pk>', views.take_exam_view, name='take-quiz'),
    path('start-quiz/<int:pk>', views.start_exam_view, name='start-quiz'),
    path('calculate-marks', views.calculate_marks_view, name='calculate-marks'),
    path('view-result', views.view_result_view, name='view-result'),
    path('check-marks/<int:pk>', views.check_marks_view, name='check-marks'),
    path('student-marks', views.student_marks_view, name='student-marks'),
    path('view-leaderboard', views.view_leaderboard_view, name='view-leaderboard'),
    path('check-score/<int:pk>', views.check_leaderboard_score_view, name='check-score'),
]
