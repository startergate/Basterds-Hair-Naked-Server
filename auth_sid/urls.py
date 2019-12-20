from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name="auth_index"),
    path('session/', views.session, name="auth_login_session"),
    path('handle/', views.login_handler, name="auth_login_handler"),
]
