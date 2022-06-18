from datetime import datetime
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    Title=models.CharField(max_length=200)
    Text=models.TextField()
    Author=models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)
    Created_date=models.DateTimeField(auto_now_add=True)
    Published_date=models.DateTimeField(default=datetime.today)

    def __str__(self):
        return self.Title
