from django import forms
from django.core import validators
from .models import User

class NewUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'

class UserProfileInfo(forms.ModelForm):
    user = models.OneToOneField(User)

    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    def __str__(self):
        return self.user.user_name
