from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

app_name = "accounts"

urlpatterns=[
    path('login/', views.login_user, name='login'),
    path('register/', views.student_signup_view, name='register'),
    path('logout/', views.logout_user, name='logout'),
]
