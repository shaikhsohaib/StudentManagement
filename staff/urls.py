from django.conf.urls import url
from .views import StaffRegisterAPI, StaffSignInAPI, ParentSignUpAPI, StudentSignUpAPI

urlpatterns = [
    url('StaffSignUp', StaffRegisterAPI.as_view()),
    url('StaffSignIn', StaffSignInAPI.as_view()),

    url('ParentRegister', ParentSignUpAPI.as_view()),
    url('StudentRegister', StudentSignUpAPI.as_view())
]
