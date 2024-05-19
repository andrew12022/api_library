from django.urls import include, path

from rest_framework import routers

from api.views import (AuthorViewSet, BookViewSet, GenreViewSet,
                       PublisherViewSet, ReviewViewSet, SeriesViewSet,
                       UserViewSet)

router_v1 = routers.DefaultRouter()

router_v1.register(
    'users',
    UserViewSet,
    basename='users',
)
router_v1.register(
    'authors',
    AuthorViewSet,
    basename='authors',
)
router_v1.register(
    'genres',
    GenreViewSet,
    basename='genrts',
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
router_v1.register(
    r'books/(?P<book_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews',
)

urlpatterns = [
    path('', include(router_v1.urls)),
    path('', include('djoser.urls')),
    # path('auth/', include('djoser.urls.authtoken')),
]
