from django.urls import path
from .views import index_view, send_message_view

urlpatterns = [
    path('', index_view, name='index'),
    path('/send-message', send_message_view, name='send_message')
]
