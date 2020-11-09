from .models import Staff
from rest_framework import serializers
from django.contrib.auth import authenticate


class StaffRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = [
            "first_name",
            "last_name",
            "email",
            "password",
            "username",
            "contact",
        ]

    def create(self, validate_data):
        staff = Staff.objects.create_user(
            first_name=validate_data.pop("first_name"),
            last_name=validate_data.pop("last_name"),
            email=validate_data.pop("email"),
            password=validate_data.pop("password"),
            username=validate_data.pop("username"),
            contact=validate_data.pop("contact"),
        )
        return staff


class StaffLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    print("email is", email)
    print("password is", password)

    def validate(self, attrs):
        self.staff=authenticate(
            username=attrs.pop("email"),
            password=attrs.pop("password")
        )

        if self.staff:
            return attrs
        else:
            raise serializers.ValidationError()