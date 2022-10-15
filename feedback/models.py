import time
from django.db import models
# Create your models here.


class Feedback(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    message = models.TextField()
    date = models.DateField(auto_now_add=True, blank=True)
    time = models.TimeField(default=time.strftime("%H:%M:%S"))

    def __str__(self) -> str:
        return self.name
