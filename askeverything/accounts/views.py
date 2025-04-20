from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views import generic

"""class SignupView(generic.FormView):
    def get(self, request):
        form = UserCreationForm()

        return render(request, 'accounts/signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/questions/categories/')  # HttpResponseRedirect to your home page"""

from django.contrib import messages

'''class MainView(generic.CreateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['loginForm'] = AuthenticationForm()
        context['signupForm'] = UserCreationForm()

        return context

    def post(self, request, *args, **kwargs):
        return HttpResponse(status=403)'''

def mainView(request):
    return render(request, 'accounts/login-or-signup.html', context={'signupForm': UserCreationForm(), 'loginForm': AuthenticationForm()})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/questions/categories/')
    else:
        return HttpResponse(status=403)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponseRedirect('/questions/categories/')
    else:
        return HttpResponse(status=403)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/questions/categories/')