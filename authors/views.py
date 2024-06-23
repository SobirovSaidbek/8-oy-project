from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from authors.models import AuthorModel
from authors.serializers import AuthorSerializer


class AuthorListAPIView(APIView):
    def get(self, request):
        author = AuthorModel.objects.all()
        serializer = AuthorSerializer(author, many=True)
        response = {
            'success': True,
            'total': len(author),
            'authors': serializer.data
        }

        return Response(response)


class AuthorDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            author = get_object_or_404(AuthorModel, pk=pk)
            serializer = AuthorSerializer(author)
            response = {
                'success': True,
                'author': serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        except AuthorModel.DoesNotExist:
            response = {
                'success': False
            }
        return Response(response, status=status.HTTP_404_NOT_FOUND)

class AuthorCreateAPIView(APIView):
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'success': True,
                'messages': 'Author Created',
                'author': serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)

class AuthorUpdateAPIView(APIView):
    def put(self, request, pk):
        author = get_object_or_404(AuthorModel, pk=pk)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'success': True,
                'messages': 'Author Updated',
                'author': serializer.data
            }

            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorDeleteAPIView(APIView):
    def delete(self, request, pk):
        author = get_object_or_404(AuthorModel, pk=pk)
        author.delete()
        response = {
            'success': True,
            'messages': 'Author Deleted'
        }

        return Response(response, status=status.HTTP_204_NO_CONTENT)