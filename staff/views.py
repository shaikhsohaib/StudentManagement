# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# from django.shortcuts import render

from rest_framework.generics import (CreateAPIView, GenericAPIView, UpdateAPIView)

from .serializers import (StaffRegisterSerializer, StaffLoginSerializer, StaffUpdateSerializer)
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


class StaffUpdateAPI(UpdateAPIView):
    serializer_class = StaffUpdateSerializer

    def get_queryset(self):
        stu_id = self.kwargs['pk']
        return Staff.objects.filter(id=stu_id)

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.firstname = request.data["firstname"]
        instance.lastname = request.data["lastname"]
        instance.age = request.data["age"]
        instance.gender = request.data["gender"]
        # instance.password = request.data["password"]
        instance.email = request.data['email']

        serializer = self.get_serializer(instance, data=request.data)

        if serializer.is_valid(raise_exception=True):
            self.partial_update(serializer)

        return Response(serializer.data, status.HTTP_200_OK)





class ParentSignUpAPI(CreateAPIView):
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


class StudentSignUpAPI(CreateAPIView):
    serializer_class = StudentSerializer

    def post(self, request, *args, **kwargs):
        student_serializer = self.get_serializer(data=request.data)

        if student_serializer.is_valid():
            student_serializer.save()

            student_object = Student.objects.get(email=request.data["email"])

            student_response = {
                "id": student_object.id,
                "firstname": student_object.firstname,
                "lastname": student_object.lastname,
                "email": student_object.email,
                "gender": student_object.gender,
                "contact": student_object.contact
            }

            return Response(student_response, status.HTTP_200_OK)
        else:
            return Response(student_serializer.errors, status.HTTP_400_BAD_REQUEST)

