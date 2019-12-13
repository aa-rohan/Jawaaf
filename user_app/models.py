from django.db import models


class UserModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    karma = models.PositiveIntegerField(default=0)
    contact = models.PositiveIntegerField(default=0)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name
