from django.conf.urls import url
from staff.views import ParentSignUpAPI

urlpatterns = [
    url('ParentSignUp', ParentSignUpAPI.as_view())
]
