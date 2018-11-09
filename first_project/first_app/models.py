from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class User(models.Model):
#     user_name= models.CharField(max_length=264,unique=True)
#     email = models.EmailField(max_length=264, unique=True)
#     password = models.PassField(max)
#     def __str__(self):
#         return self.user_name




class UserProfileInfo(models.Model):

    user=models.OneToOneField(User)

    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username


