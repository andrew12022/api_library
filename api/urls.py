from django.urls import include, path

from rest_framework import routers

from api.views import (AuthorViewSet, BookViewSet, GenreViewSet,
                       PublisherViewSet, SeriesViewSet)

router_v1 = routers.DefaultRouter()

router_v1.register(
    'authors',
    AuthorViewSet,
    basename='authors',
)
router_v1.register(
    'genres',
    GenreViewSet,
    basename='genres',
)
router_v1.register(
    'series',
    SeriesViewSet,
    basename='series',
)
router_v1.register(
    'publishers',
    PublisherViewSet,
    basename='publishers',
)
router_v1.register(
    'books',
    BookViewSet,
    basename='books',
)

urlpatterns = [
    path('', include(router_v1.urls)),
]
