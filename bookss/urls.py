from django.urls import path

from bookss.views import *

urlpatterns = [
    path('', BookListAPIView.as_view(),),
    path('create/', BookCreateAPIView.as_view(),),
    path('<int:pk>/', BookDetailAPIView.as_view(),),
    path('<int:pk>/update/', BookUpdateAPIView.as_view(),),
    path('<int:pk>/delete/', BookDeleteAPIView.as_view()),
]