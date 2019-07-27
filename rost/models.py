from django.db import models

# Create your models here.
class Time(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.time)

class Online(models.Model):
    user = models.IntegerField()
    time = models.ForeignKey(Time, on_delete=models.CASCADE)
    vk = models.BooleanField(default=False)
    tg = models.BooleanField(default=False)
    def __str__(self):
        return str(self.user)