from django.urls import path
from . import views

urlpatterns = [
    path('createcasesheet/', views.createcasesheet, name="createcasesheet"),
    path('question1/', views.question1, name="question1"),
    path('question2/', views.question2, name="question2"),
    path('question3/', views.question3, name="question3"),
    path('question4/', views.question4, name="question4"),
    path('question5/', views.question5, name="question5"),
    path('question6/', views.question6, name="question6"),
    path('question7/', views.question7, name="question7"),
    path('question8/', views.question8, name="question8"),
    path('question9/', views.question9, name="question9"),
    path('question10/', views.question10, name="question10"),
    path('question11/', views.question11, name="question11"),
    path('question12/', views.question12, name="question12"),
    path('question13/', views.question13, name="question13"),
    path('question14/', views.question14, name="question14"),
    path('question15/', views.question15, name="question15"),
    path('question16/', views.question16, name="question16"),
    path('question17/', views.question17, name="question17")
]
