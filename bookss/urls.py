from django.urls import path

from bookss.views import *

urlpatterns = [
    path('', get_all_books,),
    path('create/', create_book_view,),
    path('<int:pk>/', get_book),
    path('<int:pk>/update/', update_book_view),
    path('<int:pk>/delete/', delete_book_view),
]