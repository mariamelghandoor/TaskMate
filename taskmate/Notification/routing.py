from django.urls import path
from .consumers import NotificationConsumer

websocket_urlpatterns = [
    path('ws/Notifications/<int:user_id>/', NotificationConsumer.as_asgi()),
]
