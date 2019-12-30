from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="api_v1_index"),
    path('<str:pid>/summary/', views.get_profile, name="api_v1_get_profile"),
    path('<str:pid>/match/', views.get_matches, name="api_v1_get_match"),
    path('match/<str:match_id>', views.get_match_specific, name="api_v1_get_match_specific")
]
