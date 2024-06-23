from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from bookss.models import BookModel
from bookss.serializers import BookSerializer


"""@api_view(['GET'])
def get_all_books(request, *args, **kwargs):
    books = BookModel.objects.all()
    data = BookSerializer(books, many=True).data
    return Response(data)"""


class BookListAPIView(generics.ListAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer


"""@api_view(['GET'])
def get_book(request, pk, *args, **kwargs):
    try:
        book = BookModel.objects.get(pk=pk)
    except BookModel.DoesNotExist:
        return Response({'message': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
    data = BookSerializer(book).data
    return Response(data)"""


class BookDetailAPIView(generics.RetrieveAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer


"""@api_view(['PUT'])
def update_book_view(request, pk, *args, **kwargs):
    try:
        book = BookModel.objects.get(pk=pk)
    except BookModel.DoesNotExist:
        return Response({'message': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = BookSerializer(book, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)"""


class BookUpdateAPIView(generics.UpdateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer

"""@api_view(['PATCH'])
def update_book_view(request, pk, *args, **kwargs):
    try:
        book = BookModel.objects.get(pk=pk)
    except BookModel.DoesNotExist:
        return Response({'message': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = BookSerializer(book, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)"""


"""@api_view(['POST'])
def create_book_view(request, *args, **kwargs):
    data = request.data
    serializer = BookSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)"""


class BookCreateAPIView(generics.CreateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer


"""@api_view(['DELETE'])
def delete_book_view(request, pk, *args, **kwargs):
    try:
        book = BookModel.objects.get(pk=pk)
    except BookModel.DoesNotExist:
        return Response({'message': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
    book.delete()

    return Response({'message': 'Book is Deleted '}, status=status.HTTP_204_NO_CONTENT)"""


class BookDeleteAPIView(generics.DestroyAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer

@api_view(['GET'])
def filter_book_view(request,  *args, **kwargs):
    book = BookModel.objects.order_by('-pages')
    data = BookSerializer(book, many=True).data
    if not book:
        return Response({'message': 'No books found'}, status=status.HTTP_404_NOT_FOUND)
    return Response(data)
