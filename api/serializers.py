from rest_framework import serializers

from books.models import Author, Book, Genre, Publisher, Series


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
