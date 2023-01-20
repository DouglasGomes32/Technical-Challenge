from django.db import models
import uuid

# Create your models here.
class CreditScore(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  user = models.ForeignKey('user.User', on_delete=models.CASCADE)

  age = models.IntegerField()
  address = models.CharField(max_length=250)
  income = models.DecimalField(max_digits=10, decimal_places=2)

  def __str__(self):
    return self.address

class Asset(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  user = models.ForeignKey('user.User', on_delete=models.CASCADE)
  description = models.CharField(max_length=50)
  value = models.DecimalField(max_digits=10, decimal_places=2)

  def __str__(self):
    return self.description

class CreditRequest(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  credit_score = models.ForeignKey('CreditScore', on_delete=models.CASCADE)

  def __str__(self):
    return self.credit_score.address
