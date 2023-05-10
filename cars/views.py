from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CarSerializer
from .models import Car

@api_view(['GET', 'POST'])
def cars_list(request):
    
    if request.method == 'GET':
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

        # if serializer.is_valid() == True:
            # serializer.save()
            #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def car_detail(request, pk):
    try:
        car = Car.objects.get(pk=pk)
        serializer = CarSerializer(car);
        return Response(serializer.data)
    
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
   
    
