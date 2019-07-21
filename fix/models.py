from django.db import models
from django.contrib.auth.models import User

class Problem(models.Model):
    name = models.CharField(max_length = 20)
    text_in = models.CharField(max_length = 50)
    text_out = models.CharField(max_length = 50)
    location = models.CharField(max_length = 20)
    status_read = models.BooleanField(default=False)
    status_complate = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like_user = models.ManyToManyField(User, through='Like', related_name = 'like_user')

    @property
    def likeint(self):
        sum = 0
        for i in list(self.like_set.all()):
            sum += i.type
        return sum
class Like(models.Model):
    type = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)