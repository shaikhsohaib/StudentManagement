# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# from django.shortcuts import render

from rest_framework.generics import (CreateAPIView, GenericAPIView)

from .serializers import (StaffRegisterSerializer, StaffLoginSerializer)
from parent.serializers import ParentSerializer
from student.serializers import StudentSerializer

from .models import Staff
from parent.models import Parent
from student.models import Student

from rest_framework import status
from rest_framework.response import Response


# Create your views here.
class StaffRegisterAPI(CreateAPIView):
    serializer_class = StaffRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            staff_object = Staff.objects.get(email=request.data["email"])
            response_data = {
                "id": staff_object.id,
                "email": staff_object.email,
                "username": staff_object.username,
                "last_login": staff_object.last_login,
                "first_name": staff_object.first_name,
                "last_name": staff_object.last_name,
                "date_joined": staff_object.date_joined
            }
            return Response(response_data, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class StaffSignInAPI(GenericAPIView):
    serializer_class = StaffLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            staff_obj = serializer.staff  # serializer.staff return email address of staff

            response_data = {
                "id": staff_obj.id,
                "username": staff_obj.username,
                "email": staff_obj.email
            }

            return Response(response_data, status.HTTP_302_FOUND)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class Parent_StudentSignUpAPI(CreateAPIView):
    serializer_class = ParentSerializer

    def post(self, request, *args, **kwargs):
        parent_serializer = self.get_serializer(data=request.data)

        if parent_serializer.is_valid():
            parent_serializer.save()

            parent_object = Parent.objects.get(email=request.data["email"])

            parent_response = {
                "id": parent_object.id,
                "firstname": parent_object.firstname,
                "lastname": parent_object.lastname,
                "gender": parent_object.gender
            }

            return Response(parent_response, status.HTTP_200_OK)
        else:
            return Response(parent_serializer.errors, status.HTTP_400_BAD_REQUEST)


