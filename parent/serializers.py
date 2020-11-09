from .models import Parent
from rest_framework import serializers


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = [
            'email',
            'password',
            'firstname',
            'lastname',
            'gender'
        ]

    # def create(self, validate_data):
    #     parent = Parent.objects.create_user(
    #         email=validate_data.pop('email'),
    #         password=validate_data.pop('password'),
    #         firstname=validate_data.pop('firstname'),
    #         lastname=validate_data.pop('lastname'),
    #         gender=validate_data.pop('gender')
    #     )
    #
    #     return parent
