# api/views.py
from rest_framework import viewsets
from .models import Task
from .serializer import TaskSerializer

class TaskListCreateView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetailView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
