from django.shortcuts import get_object_or_404

from django_filters.rest_framework import DjangoFilterBackend
from djoser.views import UserViewSet
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response

from api.permissions import IsAuthorOrReadOnly
from api.serializers import (AuthorSerializer, BookSerializer,
                             FavouritesSerializer, GenreSerializer,
                             PublisherSerializer, ReviewSerializer,
                             SeriesSerializer, UserSerializer)
from books.models import (Author, Book, Favourites, Genre, Publisher, Review,
                          Series)
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
    )
    search_fields = (
        'name',
    )

    def add_to(self, request, pk, serializer_class):
        try:
            book = Book.objects.get(
                id=pk,
            )
        except Book.DoesNotExist:
            return Response(
                {'errors': 'Книги не существует!'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        data = {
            'user': request.user.id,
            'book': book.id
        }
        serializer = serializer_class(
            data=data,
            context={'request': request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def remove_from(self, request, pk, model):
        book = get_object_or_404(
            Book,
            id=pk,
        )
        try:
            book = model.objects.get(
                user=request.user,
                book=book,
            )
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except model.DoesNotExist:
            return Response(
                {'errors': 'Книги нет!'},
                status=status.HTTP_400_BAD_REQUEST,
            )

    @action(
        detail=True,
        methods=['POST'],
        permission_classes=[IsAuthenticated],
    )
    def favourites(self, request, pk):
        return self.add_to(request, pk, FavouritesSerializer)

    @favourites.mapping.delete
    def delete_favorite(self, request, pk):
        return self.remove_from(request, pk, Favourites)

    @action(
        detail=False,
        methods=['GET'],
        permission_classes=[IsAuthenticated],
    )
    def favourites_list(self, request):
        user = request.user
        favourites = Favourites.objects.filter(user=user)
        books = Book.objects.filter(
            id__in=favourites.values_list('book'),
        )
        serializer = BookSerializer(
            books,
            many=True,
            context={'request': request},
        )
        return Response(serializer.data)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    http_method_names = ['post', 'patch', 'delete']

    def get_book(self):
        book_id = self.kwargs.get('book_id')
        return get_object_or_404(Book, id=book_id)

    def get_queryset(self):
        return self.get_book().reviews.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, book=self.get_book())
