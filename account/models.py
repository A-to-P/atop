from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

JOB_CHOICES = (("restaurant", "Restaurant"),("consultant", "Consultant"))

class UserManager(BaseUserManager):
    def create_user(self, username, password, **kwargs): # 필수
        user = self.model(username=username, **kwargs)
        user.set_password(password)
        user.save()
        
    def create_normaluser(self, username, password, **kwargs): # 필수
        self.create_user(username, password, **kwargs)
        
    def create_superuser(self, username, password, **kwargs): # 필수
        kwargs.setdefault("is_superuser", True)
        self.create_user(username, password, **kwargs)


class User( AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    
    USERNAME_FIELD = "username"
    
    # 개인정보
    username = models.CharField(unique=True, max_length=20)
    email = models.EmailField(max_length=60, default="")
    job = models.CharField(choices=JOB_CHOICES, max_length=10, null=False, blank=False)
    tag =  models.ManyToManyField('Tag', blank=True)
    point = models.IntegerField(default=0)

    
    @property
    def is_staff(self):
        return self.is_superuser


class Tag(models.Model):
    name = models.CharField(max_length=20)
    # 요식업분야/컨설팅분야 구분
    job = models.CharField(choices=JOB_CHOICES, max_length=10)

    class Meta:
        db_table = 'tag'

    def __str__(self):
        return f"{self.name}" 
