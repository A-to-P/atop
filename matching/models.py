from django.db import models
from datetime import timedelta
# Create your models here.

class Request(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    # 요식업자 정보
    user = models.ForeignKey("account.User", on_delete=models.CASCADE)
    name = models.CharField(max_length=20, default="", blank=True)
    age = models.IntegerField(default=0, blank=True)
    career = models.TextField(max_length=50, default="" , blank=True)
    
    # 요식업분야, 주메뉴, 가게위치, 가게규모, 월평균매출
    rest_tags = models.ManyToManyField("account.Tag", related_name='restaurant', blank=True)
    menu = models.CharField(max_length=25, default="", blank=True)
    location = models.CharField(max_length=25, default="", blank=True)
    area = models.CharField(max_length=25, default="", blank=True)
    monthly_avg_rev = models.IntegerField(default=0, blank=True)
    

    # 제목, 컨설팅분야, 컨설팅비, 의뢰내용
    title = models.CharField(max_length=20, default="", blank=True)
    consult_tags = models.ManyToManyField("account.Tag", related_name='consultant', blank=True)
    fee = models.IntegerField(default=0, blank=True)
    content = models.TextField(blank=True)
    
    
    @property
    def deadline(self):
        return self.created_at + timedelta(weeks=1)
    
    @property
    def summary(self):
        return self.content[:100]

    def __str__(self):
        return f"{self.title}"
    
class Application(models.Model):
    req = models.ForeignKey("matching.Request", on_delete=models.CASCADE, default=None)
    user = models.ForeignKey("account.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # 컨설팅 기획안
    proposal = models.TextField(default="", blank=True)
    
    def __str__(self):
        return f"{self.req} | {self.user}"