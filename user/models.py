from django.db import models
import uuid

# Create your models here.
class Debt(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  user = models.ForeignKey('User', on_delete=models.CASCADE)
  
  description = models.CharField(max_length=50)
  debt_value = models.DecimalField(max_digits=10, decimal_places=2)

  def __str__(self):
    return self.description

class User(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  cpf = models.CharField(max_length=11)
  name = models.CharField(max_length=50)
  address = models.CharField(max_length=250)

  def __str__(self):
    return self.name
