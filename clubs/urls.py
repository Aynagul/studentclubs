from django.urls import path
from clubs import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('student_clubs/', views.student_clubs, name="student_clubs"),
    path('student_clubs/<int:pk>', views.club_view, name="club"),
    path('news/', views.news, name='news'),
    path('home_tr/', views.home_tr, name='home_tr'),
    path('about_tr/', views.about_tr, name='about_tr'),
    path('student_clubs_tr/', views.student_clubs_tr, name="student_clubs_tr"),
    path('news_tr/ ', views.news_tr, name='news_tr'),
]
