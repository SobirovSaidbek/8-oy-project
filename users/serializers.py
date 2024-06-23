from rest_framework import serializers

from users.models import UsersModel


class UsersModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersModel
        fields = '__all__'