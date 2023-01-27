from rest_framework.serializers import ModelSerializer
from .models import Order


class OrderSerializer(ModelSerializer):

    class Meta:
        model = Order
        fields = ["user", 'art', 'status', 'order_date']
        read_only_fields = ['status']

