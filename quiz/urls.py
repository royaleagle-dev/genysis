from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'quiz'
urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('category/<int:category_id>', views.category, name='category'),
    path('dev/', TemplateView.as_view(template_name = 'quiz/development.html'), name = 'development'),
]