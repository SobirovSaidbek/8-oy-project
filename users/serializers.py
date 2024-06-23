from rest_framework import serializers

from users.models import UsersModel


class UsersModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersModel
        fields = '__all__'


class UsersSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    age = serializers.IntegerField()
    phone_number = serializers.CharField(max_length=13)

    def validate_email(self, email):
        if UsersModel.objects.filter(email=email).exists():
            raise serializers.ValidationError("This email already exists.")
        return email

    def validate_phone_number(self, phone_number: str):
        if UsersModel.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError("This phone number already exists.")

        elif len(phone_number) != 13:
            raise serializers.ValidationError("This It should not be less than 13 numbers")

        elif not phone_number.isnumeric():
            raise serializers.ValidationError("All must be numbers")

        return phone_number

    def create(self, validated_data):
        return UsersModel.objects.create(**validated_data)