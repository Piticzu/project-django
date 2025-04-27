from django.urls import path
from .views import index_view, send_message_view, bot_response_view

urlpatterns = [
    path('', index_view, name='index'),
    path('send/', send_message_view, name='send'),
    path('bot-response/', bot_response_view, name='bot-response'),
]
