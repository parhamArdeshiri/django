from django.http import HttpResponseRedirect, Http404
from django.utils.translation import gettext as _
from django.shortcuts import render, get_object_or_404
from django.views import generic

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import CategorySerializer, QuestionSerializer, AnswerSerializer

from askeverything.settings import BASE_DIR

from .models import Category, Question, Answer
from .forms import MakeCategoryForm, MakeQuestionForm, AddAnswerForm
from .DEFUALT_HTMLs import defualt_htmls


# Create your views here.

class ShowCategories(generic.ListView):
    queryset = Category.objects.all()
    template_name = 'questions/categories.html'
    context_object_name = 'categories'


class ShowQuestions(generic.ListView):
    template_name = 'questions/asked-questions.html'
    context_object_name = 'questions'

    def get_context_data(self, pk, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['category'] = Category.objects.get(pk=pk)

        return context

    def get_queryset(self, pk):
        return Question.objects.filter(category=Category.objects.get(pk=pk))

    def get(self, request, pk, *args, **kwargs):
        self.object_list = self.get_queryset(pk=pk)
        allow_empty = self.get_allow_empty()

        if not allow_empty:
            # When pagination is enabled and object_list is a queryset,
            # it's better to do a cheap query than to load the unpaginated
            # queryset in memory.
            if self.get_paginate_by(self.object_list) is not None and hasattr(
                    self.object_list, "exists"
            ):
                is_empty = not self.object_list.exists()
            else:
                is_empty = not self.object_list
            if is_empty:
                raise Http404(
                    _("Empty list and “%(class_name)s.allow_empty” is False.")
                    % {
                        "class_name": self.__class__.__name__,
                    }
                )
        context = self.get_context_data(pk=pk)
        return self.render_to_response(context)


class ShowQuestion(generic.DetailView):
    model = Question
    template_name = 'questions/asked-question.html'
    context_object_name = 'question'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.answers = Answer.objects.filter(question=kwargs['object'])
        self.len = len(kwargs['object'].text.split("\n"))
        self.LinedAnswers = [(a.text + "\n").split("\r") for a in self.answers]
        self.renderCSS(kwargs['object'].text)

        context['answers'] = self.answers
        context['LinedAnswers'] = self.LinedAnswers
        context['LinedQuestion'] = (kwargs['object'].text).split("\n")
        context['category'] = kwargs['category']
        context['categories'] = Category.objects.all()
        context['other_questions'] = [question if question.pk != kwargs['object'].pk else None for question in
                                      Question.objects.filter(category=kwargs['category'])]


        return context

    def get(self, request, CategoryPK, QuestionPK, *args, **kwargs):
        self.object = get_object_or_404(Question, category=get_object_or_404(Category, pk=CategoryPK),
                                        pk=QuestionPK)
        context = self.get_context_data(object=self.object,
                                        category=get_object_or_404(Category, pk=CategoryPK))
        return self.render_to_response(context)

    def renderCSS(self, text):
        css = f''''''

        heights = []

        with open(f"{BASE_DIR}/templates/questions/asked-question.html", "w") as f:
            f.write(defualt_htmls['asked-question'])

        for i in range(len(self.answers)):
            css += f""".Answer{i}[
                        background-color: #3498db;
                        border-radius: 10px;
                        border: 0 solid rgb(0, 0, 0);
                        width: 340px;
                        height: {len(self.LinedAnswers[i]) * 25}px;
                        position: absolute;
                        top: {i * (len(self.LinedAnswers[i]) * 25) + 61 + (i * 45)}px;
                        left: 10px;
                        box-shadow: 5px 5px 5px rgba(180, 180, 180, 60%);
                    ]"""

            heights.append(len(self.LinedAnswers[i]) * 22 + 50)

        html = defualt_htmls['asked-question'].replace("<!---->", f"""<style>
                            {css}
                            </style>""").replace("[", "{").replace("]", "}").replace("--top",
                                                                                     f"{len(text) * (len(text) // 12 if len(text) / 2 == len(text) // 2 else len(text) // 6)}px")
        print(len(text))

        with open(f"{BASE_DIR}/templates/questions/asked-question.html", "w") as f:
            f.write(html)


class MakeCategory(generic.FormView):
    def get(self, request, *args, **kwargs):
        form = MakeCategoryForm()

        return render(request, 'questions/make-category.html', {'form': form, 'categories': Category.objects.all()})

    def post(self, request, *args, **kwargs):
        form = MakeCategoryForm(request.POST)

        if form.is_valid():
            Category.objects.create(name=form.cleaned_data['name'])

            return HttpResponseRedirect('/questions/categories/')


class MakeQuestion(generic.FormView):
    def get(self, request, *args, **kwargs):
        form = MakeQuestionForm()

        return render(request, 'questions/make-asked-question.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = MakeQuestionForm(request.POST)
        if form.is_valid():
            Question.objects.create(
                category=Category.objects.get(pk=int(form.cleaned_data['category'].replace('\'', ''))),
                title=form.cleaned_data['title'], text=form.cleaned_data['text'])

            return HttpResponseRedirect(f'/questions/{int(form.cleaned_data['category'].replace('\'', ''))}')


class AddAnswer(generic.FormView):
    def get(self, request, *args, **kwargs):
        form = AddAnswerForm()

        self.question = get_object_or_404(Question, pk=kwargs['pk'])
        self.answers = Answer.objects.filter(question=self.question)
        self.LinedAnswers = [(a.text + "\n").split("\r") for a in self.answers]
        self.len = len(self.question.text.split("\n"))

        self.renderCSS()

        return render(request, 'questions/add-answer-to-a-question.html',
                      {'form': form, 'question': self.question, 'LinedQuestion': self.question.text.split("\n"),
                       'answers': self.answers, 'LinedAnswers': self.LinedAnswers})

    def post(self, request, *args, **kwargs):
        form = AddAnswerForm(request.POST)

        if form.is_valid():
            question = get_object_or_404(Question, pk=kwargs['pk'])

            Answer.objects.create(category=question.category, question=question, text=form.cleaned_data["text"])

        return HttpResponseRedirect(f"/questions/{question.category.pk}/{kwargs['pk']}/")

    def renderCSS(self):

        css = f'''.q[
        background-color: rgb(180, 180, 180);
        border-radius: 10px;
        border: solid rgb(0, 0, 0) 1px;
        width: 500px;
        height: {self.len * 25 + 105}px;
        margin-top: 5px;
        margin-left: 445px;
        ]'''

        with open(f"{BASE_DIR}/templates/questions/add-answer-to-a-question.html", "w") as f:
            f.write(defualt_htmls['add-answer-to-a-question'])

        for i in range(len(self.answers)):
            css += f""".Answer{i}[
                            background-color: rgb(180, 180, 180);
                            border-radius: 10px;
                            border: solid rgb(0, 0, 0) 1px;
                            width: 500px;
                            height: {len(self.LinedAnswers[i]) * 22}px;
                            margin-top: 50px;
                            margin-left: 445px;
                        ]""".replace("[", "{").replace("]", "}")

        html = defualt_htmls['add-answer-to-a-question'].replace("<!---->", f"""<style>
                            {css}
                            </style>""".replace("[", "{").replace("]", "}")).replace("--", f"{self.len * 25 + 65}px")

        with open(f"{BASE_DIR}/templates/questions/add-answer-to-a-question.html", "w") as f:
            f.write(html)


# API views

class CategoryListView(APIView):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionListView(APIView):
    def get(self, request, *args, **kwargs):
        questions = Question.objects.all()
        serializer = CategorySerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswerListView(APIView):
    def get(self, request, *args, **kwargs):
        answers = Answer.objects.all()
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = AnswerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailView(APIView):

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, *args, **kwargs):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        category = self.get_object(pk)
        serializer = CategorySerializer(instance=category, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        category = self.get_object(pk)
        print("Level 1 passed")
        category.delete()
        print("Level 2 passed")

        return Response(status=status.HTTP_204_NO_CONTENT)


class QuestionDetailView(APIView):

    def get_object(self, pk):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, pk, *args, **kwargs):
        question = self.get_object(pk)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        question = self.get_object(pk)
        serializer = CategorySerializer(instance=question, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        question = self.get_object(pk)
        question.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class AnswerDetailView(APIView):

    def get_object(self, pk):
        try:
            return Answer.objects.get(pk=pk)
        except Answer.DoesNotExist:
            raise Http404

    def get(self, request, pk, *args, **kwargs):
        answer = self.get_object(pk)
        serializer = AnswerSerializer(answer)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        answer = self.get_object(pk)
        serializer = AnswerSerializer(instance=answer, data=request)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        answer = self.get_object(pk)
        answer.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
