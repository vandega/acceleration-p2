from rest_framework import serializers
from .models import Delivery, Order, Answer


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ['method']


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'book', 'comment', 'delivery', 'accepted']


class OrderAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'book', 'comment', 'delivery', 'orderer', 'accepted']
        # extra_kwargs = {
        #     'book': {'read_only': True},
        #     'commit': {'read_only': True},
        #     'delivery': {'read_only': True},
        # }

