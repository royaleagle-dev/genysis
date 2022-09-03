from django.db import models

# Create your models here.

class Question(models.Model):
    text = models.CharField(max_length = 255)
    date_added = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default = 1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Answer(models.Model):
    text = models.CharField(max_length = 255)
    date_added = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    correct = models.BooleanField(default=False)

    def is_correct(self):
        return self.correct
    
    def __str__(self):
        return self.text

class Category(models.Model):
    name = models.CharField(max_length = 255)
    date_added = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default = 1)

    def __str__(self):
        return self.name
