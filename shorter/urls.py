from django.urls import path
from . import views

app_name = 'shorter'
urlpatterns = [
    path('api/v1/', views.ShorterCreateAPIView.as_view()),
]
