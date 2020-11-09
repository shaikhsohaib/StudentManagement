from django.conf.urls import url
from .views import StaffRegisterAPI, StaffSignInAPI

urlpatterns = [
    url('StaffSignUp', StaffRegisterAPI.as_view()),
    url('StaffSignIn', StaffSignInAPI.as_view())
]