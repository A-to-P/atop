from django.db import models

# Create your models here.


class Room(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    consultant = models.ForeignKey(
        "account.User", related_name='room_consultant', on_delete=models.CASCADE)
    restaurant = models.ForeignKey(
        "account.User", related_name='room_restaurant', on_delete=models.CASCADE)


class Message(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    message = models.TextField() # 카카오톡은 글자수제한이 없다고함
    user = models.ForeignKey("account.User", on_delete=models.CASCADE, related_name='message')
    room = models.ForeignKey("chat.Room", on_delete=models.CASCADE, related_name='message')
    filename = models.CharField(max_length=50, default="", blank=True)
    base64URL = models.TextField(default="", blank=True)
    
    def __str__(self) -> str:
        return f"{self.user.username} \"{self.message[:5]}{'...' if len(self.message)>5 else ''}\""
    
    def ordered_messages(self, room_id):
        return Message.objects.filter(room=room_id).order_by('created_at')