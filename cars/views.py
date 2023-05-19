from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CarSerializer
from .models import Car

@api_view(['GET', 'POST'])
def cars_list(request):
    
    if request.method == 'GET':
        dealership_name = request.query_params.get('dealership')
        sort_param = request.query_params.get('sort')
        print(dealership_name)
        cars = Car.objects.all()
        
        if dealership_name:
            cars = cars.filter(dealership__name=dealership_name)
        
        if sort_param:
            cars = cars.order_by(sort_param)
            
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

@api_view(['GET', 'PUT', 'DELETE'])
def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'GET':
        serializer = CarSerializer(car);
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CarSerializer(car, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def cars_by_make(request, make):
    cars = Car.objects.all()
    cars_make = cars.filter(make=make) 

    if cars_make:
        serializer = CarSerializer(cars_make, many=True)
        return Response(serializer.data)
    else:
        return Response("No cars of that make in the database!", status=status.HTTP_404_NOT_FOUND)
    
