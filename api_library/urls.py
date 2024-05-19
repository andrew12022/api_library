from django.contrib import admin
from django.urls import include, path, reverse_lazy
from django.views.generic.edit import CreateView

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from users.forms import UserCreationForm

schema_view = get_schema_view(
    openapi.Info(
        title="Api_library",
        default_version='v1',
        description="Документация для проекта api_library",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include('books.urls', namespace='books')),
    path('auth/', include('django.contrib.auth.urls')),
    path(
        'auth/registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=UserCreationForm,
            success_url=reverse_lazy('books:index'),
        ),
        name='registration',
    ),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

urlpatterns += [
    path(
        'swagger<format>/',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json',
    ),
    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui',
    ),
    path(
        'redoc/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc',
    ),
]
