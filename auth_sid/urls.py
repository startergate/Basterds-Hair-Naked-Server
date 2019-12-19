from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name="auth_index"),
    path('handle/', views.login_handler, name="auth_login_handler")
]
