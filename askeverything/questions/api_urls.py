from django.urls import path#, include
#from rest_framework.routers import DefaultRouter
from .views import CategoryListView, QuestionListView, AnswerListView, CategoryDetailView, QuestionDetailView , AnswerDetailView

'''router = DefaultRouter()
router.register(r'category/<int:pk>/', CategoryDetailView)
router.register(r'question/<int:pk>/', QuestionDetailView)
router.register(r'answer/<int:pk>/', AnswerDetailView)'''

urlpatterns = [
    path('categories/', CategoryListView.as_view()),
    path('questions/', QuestionListView.as_view()),
    path('answers/', AnswerListView.as_view()),
    path('categories/<int:pk>/', CategoryDetailView.as_view()),
    path('questions/<int:pk>/', QuestionDetailView.as_view()),
    path('answers/<int:pk>/', AnswerDetailView.as_view())
]