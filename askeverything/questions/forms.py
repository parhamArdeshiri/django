from django import forms
from .models import Category

class MakeCategoryForm(forms.Form):
    name = forms.CharField(max_length=20)


class MakeQuestionForm(forms.Form):
    category = forms.ChoiceField(choices=((category.pk, category.name) for category in Category.objects.all()))
    title = forms.CharField(max_length=15)
    text = forms.CharField(widget=forms.Textarea)


class AddAnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
