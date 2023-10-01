from django.urls import path
from . import views

urlpatterns = [
    path('requests/', views.OrderListAPIView.as_view(), name='personal_requests'),
    path('new/', views.BookOrderRequestAPIView.as_view(), name='book_order_create'),
    path('<int:pk>/', views.AnswerRequestAPIView.as_view(), name='answer')
]


