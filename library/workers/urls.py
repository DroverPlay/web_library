from django.urls import path
from . import views


urlpatterns = [
    path('', views.workers_home, name="workers_home"),
    path('add_workers', views.add_workers, name="add_workers")
]