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

    # @property
    # def tags(self):
    #     return self.req.consult_tags
    # @property
    # def fee(self):
    #     return self.req.fee

    def __str__(self):
        return f"{self.restaurant}&{self.consultant} ({self.start}~{self.end})"


class Review(models.Model):
    consulting = models.ForeignKey(
        "consulting.Consulting", on_delete=models.CASCADE)
    rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(default="")

    def __str__(self):
        return f"{self.consulting} | {self.rating}"

    @property
    def restaurant(self):
        return self.consulting.restaurant

    @property
    def consultant(self):
        return self.consulting.consultant
