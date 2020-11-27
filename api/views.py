from django.shortcuts import render, redirect
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
# Create your views here.

def index(request):
    return render("index.html")

@api_view(["GET"])
def apiOverview(request):
    api_urls = {
        "List": "/task-list/",
        "Detail View": "/task-detail/<str:pk>/",
        "Create": "/task-create/",
        "Update": "/task-update/<str:pk>/",
        "Delete": "/task-delete/<str:pk>",
    }

    return Response(api_urls)


@api_view(["GET"])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def taskDetail(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return redirect("http://127.0.0.1:8000/task-list/")

    return Response(serializer.data)


@api_view(["POST"])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return redirect("http://127.0.0.1:8000/task-list/")

    return Response(serializer.data)


@api_view(["DELETE"])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task_id = task.id
    task.delete()

    return Response("Task successfully deleted.")