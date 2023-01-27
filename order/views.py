from rest_framework.generics import RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
from django.core.mail import send_mail
from django.conf import settings


class OrderRetrieveView(RetrieveAPIView):

    def get(self):
        queryset = Order.objects.filter(user=self.request.user)
        serializer_class = OrderSerializer(queryset)
        return Response(serializer_class.data)


class OrderCreateView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        send_mail('Покупка', f'Здраствуйте {self.request.user.fullname}, вы изьявили желание купить картину {request.art_gallery.title}', settings.EMAIL_HOST_USER, [request.user.email])
        queryset = Order.objects.filter(user=self.request.user).update(status='processing')
