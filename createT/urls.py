from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('tournamentInfo/<str:pk_test>/', views.tournamentInfo, name='tournamentInfo'),
    path('tournamentSubmit/<str:pk_test>/', views.tournamentSubmit, name='tournamentSubmit'),
    path('training/', views.trainingPage, name='training'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.register, name='register'),
    path('findTournament/', views.findTournament, name='findTournament'),
    path('createTournament/', views.createTournament, name='createTournament'),
    path('index/', views.index, name='index'),
]
