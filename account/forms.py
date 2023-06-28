from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User


# 회원가입 폼
# 로그인 돌려보려고 만들어 놓은 것, 바꾸셔도 됩니다.
class CustomUserSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username']


# 로그인(인증) 폼
class CustomUserSigninForm(AuthenticationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username']
