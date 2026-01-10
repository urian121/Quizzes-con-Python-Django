from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('quiz/question', views.quiz_question, name='quiz_question'),
    path('quiz/submit', views.quiz_submit, name='quiz_submit'),
    path('quiz/results', views.quiz_results, name='quiz_results'),
]
