from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import UsersModel
from users.serializers import UsersModelSerializer


class UsersListAPIView(APIView):
    def get(self, request):
        users = UsersModel.objects.all()
        serializer = UsersModelSerializer(users, many=True)
        response = {
            'success': True,
            'total': len(users),
            'messages': serializer.data
        }

        return Response(response, status=status.HTTP_200_OK)


class UsersDetailAPIView(APIView):
    def get(self, pk, request):
        try:
            users = get_object_or_404(UsersModel, pk=pk)
            serializer = UsersModelSerializer(users)
            response = {
                'success': True,
                'users': serializer.data
            }

            return Response(response, status=status.HTTP_200_OK)

        except UsersModel.DoesNotExist:
            response = {
                'success': False
            }

            return Response(response, status=status.HTTP_404_NOT_FOUND)


class UsersCreateAPIView(APIView):
    def post(self, request):
        serializer = UsersModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'success': True,
                'message': 'User created successfully',
                'user': serializer.data
            }

            return Response(response, status=status.HTTP_201_CREATED)


class UsersUpdateAPIView(APIView):
    def put(self, pk,  request):
        user = get_object_or_404(UsersModel, pk=pk)
        serializer = UsersModelSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'success': True,
                'message': 'User updated successfully',
                'user': serializer.data
            }

            return Response(response, status=status.HTTP_200_OK)

        else:
            response = {
                'success': False,
                'message': 'User NO Updated'
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class UsersDeleteAPIView(APIView):
    def delete(self, request, pk):
        user = get_object_or_404(UsersModel, pk=pk)
        user.delete()
        response = {
            'success': True,
            'message': 'User deleted successfully'
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)
