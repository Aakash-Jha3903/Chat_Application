import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Room, Message
from channels.db import database_sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"
        await self.get_or_create_room()
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        room_name = data["room_name"].lower()
        username = data["username"]
        content = data["message"]

        room = await self.get_room(room_name)

        # Save the message
        message = await self.create_message(room, username, content)

        # Broadcast the message
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat.message",
                "id": message.id,
                "username": message.username,
                "content": message.content,
                "user_deleted": message.user_deleted,
                "timestamp": message.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            }
        )

    async def chat_message(self, event):
        """Send message to WebSocket"""
        await self.send(text_data=json.dumps({
            "type": "chat.message",
            "id": event["id"],
            "username": event["username"],
            "content": event["content"],
            "user_deleted": event["user_deleted"],
            "timestamp": event["timestamp"],
        }))

    async def chat_message_deleted(self, event):
        """Send deleted message notification"""
        await self.send(text_data=json.dumps({
            "type": "chat.message_deleted",
            "msg_id": event["msg_id"]
        }))

    @database_sync_to_async
    def get_or_create_room(self):
        return Room.objects.get_or_create(name=self.room_name)

    @database_sync_to_async
    def get_room(self, room_name):
        return Room.objects.get_or_create(name=room_name)[0]

    @database_sync_to_async
    def create_message(self, room, username, content):
        return Message.objects.create(room=room, username=username, content=content)

