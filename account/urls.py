from django.urls import path
from .views import RegistrationAPIView

urlpatterns = [
    path('user/create', RegistrationAPIView.as_view())
]
