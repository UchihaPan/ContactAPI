from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class contact(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    country_code=models.CharField(max_length=255)
    first_name=models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number=models.CharField(max_length=255)
    is_favourite=models.BooleanField(default=True)

    def __str__(self):
        return str(self.owner.username)