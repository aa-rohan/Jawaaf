from django.urls import path
from qna_app import views

urlpatterns = [
    path('question/', views.questions)
]
