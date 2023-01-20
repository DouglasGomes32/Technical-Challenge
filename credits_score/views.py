# Create your views here.
from rest_framework import viewsets, generics, filters

from rest_framework.response import Response
from rest_framework import status

from credits_score.serializers import CreditScoreSerializer, AssetSerializer, CreditRequestSerializer

from credits_score.models import CreditScore, Asset, CreditRequest
from user.models import User

# Create your views here.

class AssetViewSet(viewsets.ModelViewSet):
  queryset = Asset.objects.all()
  serializer_class = AssetSerializer

  def get_queryset(self):
    return Asset.objects.all()

class CreditRequestViewSet(viewsets.ModelViewSet):
  queryset = CreditRequest.objects.all()
  serializer_class = CreditRequestSerializer

  def get_queryset(self):
    return CreditRequest.objects.all()

  def create(self, request): 
    serializer = CreditRequestSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreditScoreViewSet(viewsets.ModelViewSet):
  queryset = CreditScore.objects.all()
  serializer_class = CreditScoreSerializer

  def get_queryset(self):
    cpf = self.request.query_params.get('cpf')
    if cpf is not None:
      # serializer = CreditRequestSerializer(data=self.request.data)

      # if serializer.is_valid():
      #   serializer.save()

      user_id = User.objects.get(cpf=cpf).id

      return CreditScore.objects.filter(user=user_id)

    return CreditScore.objects.all()

  def create(self, request):
    age = int(request.data.get('age'))
    income = float((request.data.get('income')))
    
    if age < 18:
      return Response({'message': 'Age must be greater than 18'}, status=status.HTTP_400_BAD_REQUEST)
    
    if income < 0:
      return Response({'message': 'Income must be greater than 0'}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = CreditScoreSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
