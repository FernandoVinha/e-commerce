from django.contrib.auth.models import AbstractUser
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return str(self.name)


class User(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING,null = True)

