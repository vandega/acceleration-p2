from django.urls import path
from . import views

"""
!!! new_genre and new_condition are for AdminUsers
"""

urlpatterns = [
    path('genre/', views.GenreListAPIView.as_view(), name='genre_list'),
    path('genre/new/', views.GenreCreateAPIView.as_view(), name='genre_create'),
    path('genre/<int:pk>/', views.GenreDetailsView.as_view(), name='genre_details'),

    path('condition/', views.ConditionListAPIView.as_view(), name='condition_list'),
    path('condition/new/', views.ConditionCreateAPIview.as_view(), name='condition_new'),
    path('condition/<int:pk>/', views.ConditionDetailsAPIView.as_view(), name='condition_details'),

    path('author/', views.AuthorListAPIView.as_view(), name='author_list_or_create'),
    path('author/<int:pk>/', views.AuthorDetailsAPIView.as_view(), name='author_details'),

    path('', views.BookListAPIView.as_view(), name='book_list_or_create'),
    path('<int:pk>/', views.BookDetaildAPIView.as_view(), name='book_details'),

    path('filter/', views.MultiModelListView.as_view(), name='filter')
    ]