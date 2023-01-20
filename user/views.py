from rest_framework import viewsets, generics, filters
from user.serializers import UserSerializer, DebtSerializer
from user.models import User, Debt
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from validate_docbr import CPF

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [permissions.IsAuthenticated]

  def get_queryset(self):
    queryset = User.objects.all()

    cpf = self.request.query_params.get('cpf')
    if cpf is not None:
      queryset = User.objects.filter(cpf=cpf)

    return queryset

  def create(self, request):
    cpf = request.data.get('cpf')

    cpf_already_exist = User.objects.filter(cpf=cpf).exists()

    if cpf_already_exist:
      return Response({'message': 'CPF already exists'}, status=status.HTTP_400_BAD_REQUEST)

    if not CPF().validate(cpf):
      return Response({'message': 'Invalid CPF'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

class DebtViewSet(viewsets.ModelViewSet):
  queryset = Debt.objects.all()
  serializer_class = DebtSerializer

  def get_queryset(self):
    return Debt.objects.all()

  def create(self, request):
    debt_value = float(request.data.get('debt_value'))

    if debt_value is not None and debt_value < 0.0:
      return Response({'message': 'Debt value must be greater than zero'}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = DebtSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
