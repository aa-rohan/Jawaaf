from django.urls import path
from user_app import views
app_name = 'user'

urlpatterns = [
    path('login/', views.loginauth, name='login'),
    path('logout/', views.logout, name='logout'),
]
