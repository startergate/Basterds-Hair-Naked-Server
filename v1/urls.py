from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="api_v1_index"),
    path('summary/<str:pid>/', views.get_profile, name="api_v1_get_profile"),
]
