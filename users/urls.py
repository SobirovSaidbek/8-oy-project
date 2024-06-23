from django.urls import path
from users.views import *


urlpatterns = [
    path('', UsersListAPIView.as_view()),
    path('create/', UsersCreateAPIView.as_view()),
    path('<int:pk>/', UsersDetailAPIView.as_view()),
    path('<int:pk>/update/', UsersUpdateAPIView.as_view()),
    path('<int:pk>/delete/', UsersDeleteAPIView.as_view())
]