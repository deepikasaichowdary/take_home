# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskListCreateView, TaskDetailView

router = DefaultRouter()
router.register(r'tasks', TaskListCreateView, basename='task')
router.register(r'task', TaskDetailView, basename='task_detail')

urlpatterns = [
    path('', include(router.urls)),
]
