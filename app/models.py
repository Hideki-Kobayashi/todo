from django.db import models

# Create your models here.
class Contribution(models.Model):
    theme = models.CharField(max_length=100)
    deadline = models.CharField(max_length=100)
    memo = models.TextField(null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.theme