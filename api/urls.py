from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path("sensor-data/", views.getSensorData, name="get-sensor-data"),
    path("sensor-data/<str:name>/", views.getSensorDataByName, name="get-sensor-data-by-name"),
    path("camera/feed/", views.cameraFeed, name="cameraFeed"),
    path("task-list/", views.taskList, name="task-list"),
    path("task-detail/<str:pk>/", views.taskDetail, name="task-detail"),
    path("task-create/", views.taskCreate, name="task-create"),
    path("task-update/<str:pk>/", views.taskUpdate, name="task-update"),
    path("task-delete/<str:pk>/", views.taskDelete, name="task-delete")
]

