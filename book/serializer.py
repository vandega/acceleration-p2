import django_filters
from django_filters import FilterSet
from rest_framework import serializers
from . import models
from .models import Book


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genre
        fields = ['id', 'genre']


class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Condition
        fields = ['id', 'condition']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = ['id', 'first_name', 'last_name', 'b_day', 'image']

    def create(self, validated_data):
        author = models.Author(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            b_day=validated_data['b_day'],
            image=validated_data.get('image')
        )

        author.save()
        return author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ['id', 'title', 'description', 'pages', 'author', 'genre', 'condition', 'image', 'is_available', 'owner']


class MultiModelFilter(FilterSet):
    book_title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    # author_name = django_filters.CharFilter(field_name='first_name', lookup_expr='icontains')

    class Meta:
        model = Book
        fields = []
