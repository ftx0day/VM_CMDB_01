from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        # ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"

