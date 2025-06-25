from rest_framework.response import Response
from rest_framework import status   
from django.http import Http404
from rest_framework import generics
from .models import Room, Message
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .serializers import RoomSerializer, MessageSerializer

class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class MessageList(generics.ListCreateAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        room_name = self.kwargs['room_name'].lower()
        room, _ = Room.objects.get_or_create(name=room_name)
        return Message.objects.filter(room=room)
    

class DeleteMessage(generics.DestroyAPIView):
    serializer_class = MessageSerializer
    lookup_url_kwarg = "msgID"

    def delete(self, request, *args, **kwargs):
        """Override delete to perform permission checking."""
        msg_id = self.kwargs.get("msgID")
        username = self.kwargs.get("username")
        room_name = self.kwargs.get("roomName").lower()

        try:
            print("request.data:", request.data)
            message = Message.objects.get(id=msg_id)
            print("message:", message)
        except Message.DoesNotExist:
            return Response({"error": "Message does not exist"}, status=status.HTTP_404_NOT_FOUND)

        # Check ownership
        if message.username != username:
            return Response({"error": "You are not the owner of this message"}, status=status.HTTP_403_FORBIDDEN)

        # message.delete()
        message.user_deleted = True
        message.content = "This message has been deleted"
        message.save()  
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f'chat_{room_name}',
            {
                "type": "chat.message_deleted",
                "msg_id": msg_id,
            }
        )

        return Response({"message": "Message deleted successfully"}, status=status.HTTP_204_NO_CONTENT)