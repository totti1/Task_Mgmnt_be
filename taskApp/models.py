from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=30)
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.project_name

class Task(models.Model):
    task_name = models.CharField(max_length=30)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    assignee = models.ManyToManyField(User)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    priority = models.CharField(max_length=30)
    file_for_task = models.CharField(max_length=50)


    def __str__(self):
        return self.task_name