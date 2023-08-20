from django.urls import path
from . import views

app_name = 'chats'

urlpatterns = [
    path('chat/', views.chat_view, name='chat_view'),
    path('get_recommendation/', views.get_recommendation,
         name='get_recommendation'),
]
