from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Usersfield(models.Model):
    name = models.CharField(max_length=125)
    email = models.EmailField(max_length=125)

    def __str__(self):
        return self.name


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=125)
    profile_pic = models.ImageField(upload_to='profile pic',blank=True)


class Post(models.Model):
     Title = models.CharField(max_length=125)
     text_description =models.CharField(max_length=125)

     def __str__(self):
            return self.Title







