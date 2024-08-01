from django.urls import path
from . import views

urlpatterns = [
    path('', views.exam_list, name='exam_list'),
    path('take_exam/<int:exam_id>/', views.take_exam, name='take_exam'),
    path('exam_result/<int:result_id>/', views.exam_result, name='exam_result'),
]
