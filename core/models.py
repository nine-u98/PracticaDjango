from django.db import models

# Create your models here.
class IpUsers(models.Model):
    ip_user = models.CharField(max_length=32)

    def __str__(self):
        return self.ip_user