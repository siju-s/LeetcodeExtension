from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=60)
    username = models.CharField(max_length=60)
    rank = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    avatar = models.ImageField(default='')

    def __str__(self):
        return self.username


class QuestionsSolved(models.Model):
    easyCount = models.IntegerField(default=0)
    mediumCount = models.IntegerField(default=0)
    hardCount = models.IntegerField(default=0)
    totalCount = models.IntegerField(default=0)
    easySolvedCount = models.IntegerField(default=0)
    mediumSolvedCount = models.IntegerField(default=0)
    hardSolvedCount = models.IntegerField(default=0)
    totalSolvedCount = models.IntegerField(default=0)

