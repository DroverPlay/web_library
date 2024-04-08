from django.urls import path
from . import views


urlpatterns = [
    path('', views.fundrefill, name="fundrefill"),
    path('add_fund/', views.add_fundrefill, name="add_fundrefill")
]