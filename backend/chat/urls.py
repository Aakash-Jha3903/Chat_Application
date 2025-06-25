from django.urls import path
from . import views

urlpatterns = [
    path('rooms/', views.RoomList.as_view()),
    path('rooms/<slug:room_name>/messages/', views.MessageList.as_view()),
    path('rooms/<str:roomName>/deleteMessage/<int:msgID>/<str:username>/', views.DeleteMessage.as_view(), name='delete-message'),
]