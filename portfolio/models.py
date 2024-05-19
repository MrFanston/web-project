from django.db import models
from django.contrib.auth.models import User

class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Содержимое')

    def __str__(self):
        return self.user.username + "'s Portfolio"
