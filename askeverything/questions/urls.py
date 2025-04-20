from django.urls import path
from .views import ShowCategories, ShowQuestions, ShowQuestion, MakeCategory, MakeQuestion, AddAnswer


urlpatterns = [
    path('categories/', ShowCategories.as_view()),
    path('<int:pk>/', ShowQuestions.as_view()),
    path('<int:CategoryPK>/<int:QuestionPK>/', ShowQuestion.as_view()),
    path('categories/create/', MakeCategory.as_view()),
    path('create/', MakeQuestion.as_view()),
    path('<int:pk>/answers/add/', AddAnswer.as_view())
]