from rest_framework import serializers
from user.models import *


class DebtSerializer(serializers.ModelSerializer):
  class Meta:
    model = Debt
    fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'
  