from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return  self.name

class Question(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    title = models.CharField(max_length=70)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'questions'

class Answer(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'answers'
