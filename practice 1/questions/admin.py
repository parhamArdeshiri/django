from django.contrib import admin
from .models import Question, Answer

# Register your models here.

class Inline(admin.StackedInline):
    model = Answer
    fields = ['text']
    extra = 0

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_time']
    inlines = [Inline]

