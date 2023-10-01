from rest_framework import generics, status
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from book.serializer import BookSerializer
from bookgiveaway import settings
from giveaway.models import Order
from giveaway.serializer import OrderCreateSerializer, OrderAnswerSerializer


class OrderListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrderAnswerSerializer
    queryset = Order.objects.all()

    def get_queryset(self):
        return Order.objects.filter(book__owner=self.request.user)


class BookOrderRequestAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderCreateSerializer

    def perform_create(self, serializer):
        user = self.request.user
        book = serializer.validated_data['book']
        book_owner = book.owner
        book_avelable = book.is_available
        if user != book_owner and book_avelable is True:
            # amoqmedeba im shentxvevashi tu tavis wigns ar ichuqebs
            serializer.save()
            # daaseiva motxovna
            return Response(status=status.HTTP_201_CREATED)

        return Response(data={'error: You cant order your own diploma'}, status=status.HTTP_400_BAD_REQUEST)


class AnswerRequestAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderAnswerSerializer
    queryset = Order.objects.all()

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.book.owner == request.user and instance.book.is_available:
            instance.accepted = True
            instance.book.owner = instance.orderer
            instance.book.is_available = False
            instance.save()
            instance.book.save()
            instance.delete()
            return Response(data={'order deleted'}, status=status.HTTP_200_OK)




