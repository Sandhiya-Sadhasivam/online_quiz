from django.contrib import admin
from django.urls import path, include

from quiz import views

app_name = "quiz"

urlpatterns = [
    path('list', views.student_exam_view, name='quiz-list'),
    path('take-quiz/<int:pk>', views.take_exam_view,name='take-quiz'),
]
