from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    #  first_name, last_name, email, username, password
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=150, verbose_name='adress')
    image = models.ImageField(upload_to='user_images/', null=True, blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.email}'
