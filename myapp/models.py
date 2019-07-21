from django.db import models

# Create your models here.
class Poem(models.Model):
    def __str__(self):
       return 'Name: {}, ended: {}'.format(self.name, str(self.ended))
    name = models.CharField(max_length = 50)
    ended = models.BooleanField(default=False)
    text = models.TextField()
class Abzac(models.Model):
    def __str__(self):
       return 'Poem: {}'.format(self.poem)
    poem = models.ForeignKey(Poem, on_delete=models.CASCADE)
    people = models.CharField(max_length = 30)
    text = models.TextField()