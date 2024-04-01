from django.urls import path
from . import views


urlpatterns = [
    path('', views.libraries_home, name="libraries_home"),
    path('add_libraries', views.add_libraries, name="add_libraries")
]