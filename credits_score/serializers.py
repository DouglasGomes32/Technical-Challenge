from rest_framework import serializers
from credits_score.models import *

class CreditScoreSerializer(serializers.ModelSerializer):
  class Meta:
    model = CreditScore
    fields = '__all__'

class AssetSerializer(serializers.ModelSerializer):
  class Meta:
    model = Asset
    fields = '__all__'

class CreditRequestSerializer(serializers.ModelSerializer):
  class Meta:
    model = CreditRequest
    fields = '__all__'
