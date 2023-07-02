from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from consulting.models import Consulting

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
    
    def count_consulting(self):
        return len(Consulting.objects.filter(consultant=self))
    
    def __lt__(self, other):
        return self.count_consulting() < other.count_consulting()


class Tag(models.Model):
    name = models.CharField(max_length=20)
    value = models.CharField(max_length=20, default="")
    # 요식업분야/컨설팅분야 구분
    job = models.CharField(choices=JOB_CHOICES, max_length=10)

    class Meta:
        db_table = 'tag'

    def __str__(self):
        return f"{self.name}" 

class RestaurantProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # 자기소개
    # 이름, 나이, 경력
    name = models.CharField(max_length=20, default="")
    birth = models.DateField(null=True)
    career = models.CharField(max_length=25, default="")
    self_introducing = models.TextField(max_length=500, default="") # 500자
    image = models.ImageField(upload_to='profile/', null=True, blank=True)
    
    # 컨설팅 정보
    # 연락가능시간, 가게위치, 주메뉴, 규모
    contact_at = models.TextField(max_length=200, default="")
    location = models.CharField(max_length=25, default="")
    menu = models.CharField(max_length=25, default="")
    area = models.CharField(max_length=25, default="")

    # 사업자 등록 번호 인증 
    # @property
    # def business_registration(self):
    #     pass
    
    class Meta:
        db_table = 'restaurant_profile'

    def __str__(self):
        return f"{self.user.username} | {self.name}"

class ConsultantProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # 자기소개
    # 이름, 나이, 학력, 학교    
    name = models.CharField(max_length=20, default="")
    birth = models.DateField(null=True)
    education = models.CharField(max_length=25, default="")
    self_introducing = models.TextField(max_length=500, default="") # 500자
    image = models.ImageField(upload_to='profile/', null=True, blank=True)
    # 연락가능시간
    contact_at = models.TextField(max_length=200, default="")
    
    # 학교인증은 따로 DB만들어서 사진 올리기
    # edu_verification = { 0:아직 인증 시도 안함, 1:인증사진은 올렸는데 인증이 안됨, 2:인증됨, 
    # 3:운영진이확인했는데문제가있음..? 나중여 여유되면 개발}
    @property
    def edu_verification(self):
        # DB에서 인증내역 찾아보기 (인증사진을 올리면 DB에 인증내역 생성됨)
        item = EduVerification.objects.filter(user=self.user).first()
        
        # 만약 인증 사진을 올린적이 있다면
        if item is not None:
            # 사진은 올렸지만 운영진이 확인 안함
            if item.verified == False:
                return 1            
            # 사진을 운영진이 확인했고 인증됨
            return 2
        
        # 인증내역없음, 인증시도안함
        return 0
    
    class Meta:
        db_table = 'consultant_profile'

    def __str__(self):
        return f"{self.user.username} | {self.name}"
    
    
class EduVerification(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    img = models.ImageField(upload_to='edu_verification/', null=False)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} | {self.verified}"