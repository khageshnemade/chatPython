from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static
schema_view = get_schema_view(
    openapi.Info(
        title="Chat API",
        default_version="v1",
        description="API documentation for your Django chat project",
    ),
    public=True,  # ✅ Make Swagger public
    permission_classes=(permissions.AllowAny,),  # ✅ No auth required for Swagger docs
)

urlpatterns = [
    # ✅ Swagger Docs (no login required)
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),

    # 🔐 JWT Auth
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Admin + App Routes
    path('admin/', admin.site.urls),
    path('chat/', include('chatapp.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Only used if needed
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)