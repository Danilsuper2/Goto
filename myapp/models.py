from django.db import models

# Create your models here.
class Poem(models.Model):
    name = models.CharField(max_length = 50)
    ended = models.BooleanField(default=False)
    text = models.TextField()
class Abzac(models.Model):
    poem = models.ForeignKey(Poem, on_delete=models.CASCADE)
    people = models.CharField(max_length = 30)
    text = models.TextField()