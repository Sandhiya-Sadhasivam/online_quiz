from django.urls import path
from . import views

urlpatterns = [
    path('generate', views.generate, name='generate'),
    path('verify/<str:slug>', views.verify, name='verify'),

]
