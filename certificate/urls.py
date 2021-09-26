from django.urls import path
from . import views

urlpatterns = [
    path('generate', views.generate, name='generate'),
    path('verify/<str:slug>', views.verify, name='verify'),
    path('appreciation-generate', views.appreciation_generate, name='appreciation-generate'),
    path('appreciation-verify/<str:slug>', views.appreciation_verify, name='verify'),

]
