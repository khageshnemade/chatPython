from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chatapp.urls')),
        path('accounts/', include('django.contrib.auth.urls')),  # 👈 Add this line
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

]
