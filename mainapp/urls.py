from django.urls import path
from .views import index_view, send_message_view, scroll_anchor_view

urlpatterns = [
    path('', index_view, name='index'),
    path('send/', send_message_view, name='send'),
    path('scroll-anchor/', scroll_anchor_view, name='scroll-anchor'),
]
