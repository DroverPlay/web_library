from django.urls import path
from . import views


urlpatterns = [
    path('', views.literaturetype_home, name="literaturetype_home"),
    path('add_libraries', views.add_literaturetype, name="add_literaturetype")
]