from django_filters.rest_framework import DjangoFilterBackend
from djoser.views import UserViewSet
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from api.serializers import (AuthorSerializer, BookSerializer, GenreSerializer,
                             PublisherSerializer, SeriesSerializer,
                             UserSerializer)
from books.models import Author, Book, Genre, Publisher, Series
from users.models import User


class UserViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = (
        SearchFilter,
    )
    search_fields = (
        'name',
    )


class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (
        SearchFilter,
    )
    search_fields = (
        'name',
    )


class SeriesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    filter_backends = (
        SearchFilter,
    )
    search_fields = (
        'name',
    )


class PublisherViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    filter_backends = (
        SearchFilter,
    )
    search_fields = (
        'name',
    )


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
    )
    filterset_fields = (
        'author',
        'genre',
        'series',
        'publisher',
        'availability',
    )
    search_fields = (
        'name',
    )
