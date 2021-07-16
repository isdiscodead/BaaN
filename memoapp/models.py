from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Memo(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comment')
    title = models.CharField(max_length=200, null=True)
    content = models.TextField(null=False)
    image = models.ImageField(upload_to='article/', null=False)

    created_at = models.DateField(auto_now=True)