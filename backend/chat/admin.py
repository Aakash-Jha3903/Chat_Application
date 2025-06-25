from django.contrib import admin
from .models import Room, Message

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'room', 'username', 'content', 'timestamp')
    search_fields = ('room__name', 'username', 'content')
    list_filter = ('timestamp',)
    ordering = ('timestamp',)
