from django.urls import path

from . import views

urlpatterns = [
    path("user_data", views.upload_file),
    path("task_status", views.check_task_status),
    
]