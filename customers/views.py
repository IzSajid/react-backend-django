from customers.models import Customer
from django.http import JsonResponse
from customers.serializer import CustomerSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#customers list
@api_view(['GET', 'POST'])
def customers(request):
    data = Customer.objects.all()
    serializer = CustomerSerializer(data, many=True)
    return Response({'customers': serializer.data})

#customer section
@api_view(['GET', 'POST', 'DELETE'])
def customer(request, id):
    try:
        data = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
        return Response({'message': 'The customer does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CustomerSerializer(data, many=False)
        return Response({'customer': serializer.data}, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        data.delete()
        return Response({'message': 'Customer was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
   