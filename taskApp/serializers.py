from rest_framework import serializers
from .models import Task, Project

class TaskSerializer:
    class Meta:
        model = Task
        fields = [
            "task_name",
            "description",
            "start_date",
            "end_date",
            "assignee",
            "project",
            "priority",
            "file_for_task"
        ]

class ProjectSerializer:
    class Meta:
        model = Project
        fields = [
            "project_name",
            "description",
        ]