from django.conf.urls import url
from .views import StaffRegisterAPI, StaffSignInAPI, Parent_StudentSignUpAPI

urlpatterns = [
    url('StaffSignUp', StaffRegisterAPI.as_view()),
    url('StaffSignIn', StaffSignInAPI.as_view()),

    url('Parent_StudentRegister', Parent_StudentSignUpAPI.as_view())
]