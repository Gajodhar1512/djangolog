from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    gender_choices = (
        ('Male', 'Male'),
        ('Female', "Female"),
        ('Other', 'Other')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)  # if user is del profile is also deltd but reverse z nt
    profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics')
    gender = models.CharField(max_length=10, default='Male', choices=gender_choices)

    def __str__(self):
        return f'{ self.user.username } profile'
