from django.db import models
from django.conf import settings

class Poll(models.Model):
  question = models.CharField(max_length=250)
  slug = models.SlugField(max_length=50, unique=True)
  
  def __str__ (self):
    return self.question

  
class Choice(models.Model):
  answer = models.CharField(max_length=100)
  votes = models.IntegerField()
  
  poll = models.ForeignKey(Poll)
  author = models.ForeignKey(settings.AUTH_USER_MODEL)
  
  def __str__ (self):
    return self.answer

