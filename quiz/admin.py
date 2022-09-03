from django.contrib import admin
from quiz.models import Question, Answer, Category

# Register your models here.
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Category)
