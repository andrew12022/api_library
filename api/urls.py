from django.urls import include, path

from rest_framework import routers

from api.views import BookViewSet

router_v1 = routers.DefaultRouter()

router_v1.register(
    'books',
    BookViewSet,
    basename='books',
)

urlpatterns = [
    path('', include(router_v1.urls)),
]
