from django.urls import path
from qna_app import views
app_name = 'qna'

urlpatterns = [
    path('read/', views.questionlist, name='read'),
    path('popular/', views.popular),
    path('add/', views.addquestion, name='add'),
    path('update/<int:id>/', views.update_question, name='update'),
    path('delete/<int:id>/', views.delete_question, name='delete'),
    path('vote/<int:id>/', views.vote_question, name='vote_qn'),
    path('ans/<int:id>/', views.answer, name='answer'),
    path('submit/<int:id>/', views.submit, name='submit'),
    path('detail/<int:id>/', views.detail, name='qna.detail'),
    # path('listview/', views.QuestionListViews.as_view(), name='qnlist'),
]
