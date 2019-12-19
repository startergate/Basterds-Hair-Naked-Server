from django.urls import path, include

from . import views

urlpatterns = [
    path('auth/', include('auth.urls')),
    path('', views.index, name="api_index"),
    path('<str:pid>/profile', views.get_profile, name="api_get_profile"),
]
