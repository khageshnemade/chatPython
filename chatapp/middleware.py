# chatapp/middleware.py

from urllib.parse import parse_qs
from channels.middleware import BaseMiddleware  # ✅ safer and works across versions
from django.contrib.auth.models import AnonymousUser
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from jwt import decode as jwt_decode
from django.conf import settings

class JWTAuthMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        query_string = scope["query_string"].decode()
        token = parse_qs(query_string).get("token", [None])[0]

        if token is None:
            scope["user"] = AnonymousUser()
            return await super().__call__(scope, receive, send)

        try:
            validated_token = JWTAuthentication().get_validated_token(token)
            user = JWTAuthentication().get_user(validated_token)
            scope["user"] = user
        except Exception as e:
            print("JWT authentication failed:", e)
            scope["user"] = AnonymousUser()

        return await super().__call__(scope, receive, send)
