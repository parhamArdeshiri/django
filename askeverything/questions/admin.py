from django.contrib import admin
from .models import Category, Question, Answer

# Register your models here.

class AnswersInline(admin.StackedInline):
    model = Answer
    fields = ['text']
    extra = 0

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'title', 'created_time']
    search_fields = ['category', 'title']
    inlines = [AnswersInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
