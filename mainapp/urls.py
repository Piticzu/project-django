from django.urls import path
from .views import chatgpt_view

urlpatterns = [
    path('', chatgpt_view, name='chat')
]
