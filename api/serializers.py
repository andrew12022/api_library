from django.shortcuts import get_object_or_404

from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from books.models import (Author, Book, Favourites, Genre, Publisher, Review,
                          Series)
from users.models import User


class UserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'last_name',
            'first_name',
            'middle_name',
            'username',
            'gender',
            'date_of_birthday',
            'password',
        )


class UserSerializer(UserSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'id',
            'last_name',
            'first_name',
            'middle_name',
            'username',
            'gender',
            'date_of_birthday',
        )


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        exclude = (
            'slug',
        )


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        exclude = (
            'slug',
        )


class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        exclude = (
            'slug',
        )


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        exclude = (
            'slug',
        )


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )
    book = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name',
    )

    class Meta:
        model = Review
        fields = '__all__'

    def validate(self, value):
        request = self.context['request']
        get_object_or_404(
            Book,
            id=self.context['view'].kwargs['book_id'],
        )
        if (
            request.method == 'POST'
            and request.user.reviews.all().exists()
        ):
            raise serializers.ValidationError('Ваш отзыв уже есть!')
        return value


class BookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(
        read_only=True,
    )
    genre = serializers.StringRelatedField(
        read_only=True,
    )
    series = serializers.StringRelatedField(
        read_only=True,
    )
    publisher = serializers.StringRelatedField(
        read_only=True,
    )
    reviews = serializers.StringRelatedField(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Book
        exclude = (
            'slug',
        )


class FavouritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourites
        fields = (
            'user',
            'book',
        )
        validators = [
            UniqueTogetherValidator(
                queryset=Favourites.objects.all(),
                fields=('user', 'book'),
                message='Книга уже добавлена!',
            ),
        ]

    def to_representation(self, instance):
        return BookSerializer(
            instance.book,
            context={
                'request': self.context.get('request')
            },
        ).data
