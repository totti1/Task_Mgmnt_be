from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .models import Task, Project
from .serializers import TaskSerializer, ProjectSerializer
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings

User = get_user_model()

# Create your views here.
def home(request):
    response = "You're looking at the results of question."
    return HttpResponse(response)

@api_view(['GET', 'POST'])
def tasks(request):
    if request.method == 'GET':
        user_id = Token.objects.get(key=request.auth.key).user_id
        user_info = User.objects.get(id=user_id)
        task = Task.objects.filter(user=user_info)
        data = []
        projects = []
        for item in task:
            project = Project.objects.get(id=item.project.id)
            projects.append(project)
            data.append({"id": item.id})
        
        # print(data)
        task_serializer= TaskSerializer(task, many=True)
        project_serializer = ProjectSerializer(prods, many=True)
            
        return Response({"data":task_serializer.data, "project":project_serializer.data, "status":status.HTTP_200_OK})

    elif request.method == 'POST':

        data={}
        
        user_id = Token.objects.get(key=request.auth.key).user_id

        data['task'] = request.data["task"]
        data['user'] = user_id

        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def projects(request):
    if request.method == 'GET':
        data = Project.objects.all()

        serializer = ProjectSerializer(data, many=True)

        return Response({"data":serializer.data, "status":status.HTTP_200_OK})

