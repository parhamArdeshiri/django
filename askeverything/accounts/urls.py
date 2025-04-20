from django.urls import path
from .views import mainView, signup, login, logout_view

urlpatterns = [
    path('loginorsignup/', mainView),
    path('signup/', signup),
    path('login/', login),
    path('logout/', logout_view),
]