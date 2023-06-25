from django.db import models
from account.models import User
# Create your models here.

class RestaurantProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # 자기소개
    # 이름, 나이, 경력
    name = models.CharField(max_length=20, default="")
    birth = models.DateField(null=True)
    career = models.TextField(max_length=200, default="")
    image = models.ImageField(upload_to='profile/', null=True, blank=True)
    
    # 가게소개
    # 가게위치, 주메뉴, 규모, 월평균매출
    location = models.TextField(max_length=200, default="")
    menu = models.TextField(max_length=200, default="")
    area = models.TextField(max_length=200, default="")
    avg_mothly_sales = models.TextField(max_length=200, default="")
    
    class Meta:
        db_table = 'restaurant_profile'

    def __str__(self):
        return f"{self.user.username} | {self.name}"

class ConsultantProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # 자기소개
    # 이름, 나이, 학력, 학교    
    name = models.CharField(max_length=20, null=True)
    birth = models.DateField(null=True)
    education = models.TextField(max_length=200, default="")
    college = models.TextField(max_length=200, default="")
    image = models.ImageField(upload_to='profile/', null=True, blank=True)
    # 연락가능시간
    contact_at = models.TextField(max_length=200, default="")

    class Meta:
        db_table = 'consultant_profile'

    def __str__(self):
        return f"{self.user.username} | {self.name}"