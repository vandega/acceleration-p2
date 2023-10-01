import django_filters
from django_filters import FilterSet
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .models import Genre, Book, Author, Condition
from .serializer import GenreSerializer, ConditionSerializer, AuthorSerializer, BookSerializer, MultiModelFilter


# TODO: add filter for book and author

#  views for genre -------------------------------------- [ DONE ]
class GenreListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdminUser]

    def delete(self, request, *args, **kwargs):
        genre = self.get_object()
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, *args, **kwargs):
        genre = self.get_object()
        serializer = GenreSerializer(genre, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# views for condition ----------------------------------- [ DONE ]
class ConditionListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer


class ConditionCreateAPIview(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer


class ConditionDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]

    def delete(self, request, *args, **kwargs):
        condition = self.get_object()
        condition.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, *args, **kwargs):
        condition = self.get_object()
        serializer = GenreSerializer(condition, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# views for Author -------------------------------------- [ DONE ]
class AuthorListAPIView(generics.ListAPIView, generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


# views for Book ---------------------------------------  [ DONE ]
class BookListAPIView(generics.ListAPIView, generics.CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Book.objects.filter(is_available=True)
    serializer_class = BookSerializer


class BookDetaildAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_update(self, serializer):
        if self.get_object().owner == self.request.user:
            serializer.save()
        else:
            return Response(data={f"message: You aren't allowed to edit {self.get_object().title}'s information"},
                            status=status.HTTP_400_BAD_REQUEST)

    def perform_destroy(self, instance):
        if instance.owner == self.request.user:
            instance.delete()
        else:
            return Response(data={"message: you can't dekete book"}, status=status.HTTP_400_BAD_REQUEST)


class MultiModelListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = MultiModelFilter