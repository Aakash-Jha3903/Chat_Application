from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    content = models.TextField()
    user_deleted = models.BooleanField(default=False, help_text="Indicates if the user has deleted the message")
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('timestamp',)
        
    def __str__(self):
        return f"Room: {self.room} - User: {self.username} - msg: {self.content}  Time: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"