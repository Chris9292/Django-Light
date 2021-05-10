from django.shortcuts import render, redirect
from django.http import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
from weatherbox.models import Data
from weatherbox.serializers import DataSerializer
from .database import Database

# connect to DB
db = Database()
con, cursor = db.connect()


@api_view(["GET"])
def getLatestSensorData(request):

    # search for last record added in the database and return as http response
    data = Data.objects.order_by("date")
    serializer = DataSerializer(data[len(data)-1])
    print(serializer.data)
    return Response(serializer.data)


@api_view(["GET"])
def apiOverview(request):
    api_urls = {
        "Sensor Data": "/sensor-data/",
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
        return redirect("http://127.0.0.1:8000/api/")

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return redirect("http://127.0.0.1:8000/api/")

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task_id = task.id
    task.delete()

    return Response(f"Task with id: {task_id} successfully deleted.")