from django.db import models


# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=256)
    firstName = models.CharField(max_length=128)
    lastName = models.CharField(max_length=128)
    location = models.CharField(max_length=128)

    class Meta:
        abstract = True

    def __str__(self):
        return self.email


class GeneralUser(User, models.Model):
    objects = models.Manager()

    def __str__(self):
        return self.email
