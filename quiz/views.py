from django.shortcuts import render, get_object_or_404
from quiz.models import Question, Answer, Category
from django.views.generic import ListView, DetailView

# Create your views here.

class IndexView(ListView):
    model = Category
    template_name = 'quiz/index.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.order_by('-date_added')[:10]

def category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    print(category)
    questions = Question.objects.filter(category__id=category.id)
    context = {
        'category':category,
        'questions':questions
    }
    return render(request, 'quiz/category-detail.html', context)