from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Consulting(models.Model):
    req = models.ForeignKey("matching.Request", on_delete=models.CASCADE)
    start = models.DateTimeField(default=timezone.now)
    end = models.DateTimeField(default=timezone.now, blank=True)
    consultant = models.ForeignKey(
        "account.User", related_name='consultant', on_delete=models.CASCADE)
    restaurant = models.ForeignKey(
        "account.User", related_name='restaurant', on_delete=models.CASCADE)
    done = models.BooleanField(default=False, blank=True)
    # final_report = models.FileField(upload_to='final_report', null=True, max_length=100, blank=True)
    final_report_filename = models.CharField(max_length=50, default="", blank=True)
    final_report_base64URL = models.TextField(default="", blank=True)

    # 태그 객체들의 리스트로 반환
    @property
    def tags(self):
        return list(self.req.consult_tags.all())
    
    @property
    def fee(self) -> int:
        return self.req.fee

    def __str__(self):
        return f"{self.restaurant}&{self.consultant} ({self.start}~{self.end})"


class Review(models.Model):
    consulting = models.ForeignKey(
        "consulting.Consulting", on_delete=models.CASCADE)
    rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(default="")

    def __str__(self):
        return f"{self.consulting} | {self.rating}"

    @property
    def restaurant(self):
        return self.consulting.restaurant

    @property
    def consultant(self):
        return self.consulting.consultant

class Accusation(models.Model):
    # 원고
    complainant = models.ForeignKey("account.User", related_name='complainant', on_delete=models.CASCADE)
    # 피고인
    defendant = models.ForeignKey("account.User", related_name='defendant', on_delete=models.CASCADE)
    # 증빙자료, 신고사유
    evidence = models.FileField(upload_to='evidence', null=True, max_length=100)
    comment = models.TextField(default="", blank=True)
    
    def __str__(self):
        return f"{self.id} : {self.comment[:10]}..."