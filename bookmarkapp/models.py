# from django.db import models
#
# # Create your models here.
#
from django.contrib.auth.models import User
from django.db import models


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookmark', null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    thumbnail = models.ImageField(upload_to='bookmark/', null=True)
    url = models.URLField("url", unique=True)

    def __str__(self):
        return self.title