from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers

from books.models import Author, Book, Genre, Publisher, Series
from users.models import User


class UserCreateSerializer(UserCreateSerializer):
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
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = '__all__'


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
