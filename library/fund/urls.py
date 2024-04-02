from django.urls import path
from . import views


urlpatterns = [
    path('', views.fund, name="fund"),
    path('add_fund/', views.add_fund, name="add_fund")
]