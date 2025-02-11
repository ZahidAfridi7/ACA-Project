from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),  
    path('player/', views.players, name='Players'),
    path('about/', views.about, name='About'),
    path('register/', views.register, name='Register'),
    path('feedback/',views.feedback, name='Feedback'),
]
