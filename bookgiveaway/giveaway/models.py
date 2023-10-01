from django.db import models
from book.models import Book
from bookgiveaway import settings


class Delivery(models.Model):
    method = models.CharField(max_length=50)

    def __str__(self):
        return self.method


class Order(models.Model):
    orderer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orderer')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='book')
    comment = models.TextField(default=f'Hello. I want take your book. \nWill be glad if you accepte my request. \nThank you.')
    order_data = models.DateTimeField(auto_now_add=True)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE, blank=True)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return f'Order for book {self.book.title}'


class Answer(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owner')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order')
    answer = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

# ------------------------------------------------------------------------------------------------------------------
