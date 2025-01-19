from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Chirp(models.Model):
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    def __str__(self):
        return self.message
    
    def was_edited(self):
        return self.created_at == self.updated_at
