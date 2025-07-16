import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import chatapp.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatproject.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chatapp.routing.websocket_urlpatterns
        )
    ),
})
# asgi.py
# import os
# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter, URLRouter
# from chatapp.routing import websocket_urlpatterns
# from chatapp.middleware import JWTAuthMiddleware  # ✅ Custom JWT middleware

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatproject.settings')

# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": JWTAuthMiddleware(  # 👈 Use custom middleware here
#         URLRouter(websocket_urlpatterns)
#     ),
# })
