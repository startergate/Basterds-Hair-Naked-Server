from django.urls import path, include

from . import views

urlpatterns = [
    path('auth/', include('auth.urls')),
    path('v1/', include('v1.urls')),
    path('', views.index, name="api_index"),
]
