from .views import OrderRetrieveView, OrderCreateView
from django.urls import path

urlpatterns = [
    path("order", OrderRetrieveView.as_view()),
    path("order/post", OrderCreateView.as_view())
]