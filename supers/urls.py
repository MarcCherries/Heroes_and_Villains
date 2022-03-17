from django.urls import path
from . import views

urlpatterns = [
    path('', views.character_list),
    path('<int:pk', views.character_detail)
]