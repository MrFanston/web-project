from django.db import models
from django.contrib.auth.models import User

class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    achievements = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.achievements
