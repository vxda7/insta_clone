from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django.contrib.auth import get_user_model


class CostomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        

class CostomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()    # User를 반환 settings에 있는 AUTH_USER_MODEL
        # settings.AUTH_USER_MODEL = 'accounts.user' 은 스트링을 갖는 변수이다.
        # model안에 넣어야하는건 클래스이므로 get_user_model()로 적어준다.
        fields = ('email', 'first_name', 'last_name',)