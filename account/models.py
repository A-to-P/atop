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

# class RestaurantProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
#     # 자기소개
#     # 이름, 나이, 경력
#     name = models.CharField(max_length=20, default="")
#     birth = models.DateField(null=True)
#     career = models.TextField(max_length=200, default="")
#     image = models.ImageField(upload_to='profile/', null=True, blank=True)
    
#     # 가게소개
#     # 가게위치, 주메뉴, 규모, 월평균매출
#     location = models.TextField(max_length=200, default="")
#     menu = models.TextField(max_length=200, default="")
#     area = models.TextField(max_length=200, default="")
#     avg_mothly_sales = models.TextField(max_length=200, default="")
    
#     class Meta:
#         db_table = 'restaurant_profile'

#     def __str__(self):
#         return f"{self.user.username} | {self.name}"

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