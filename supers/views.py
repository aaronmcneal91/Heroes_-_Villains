
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import supers
from .serializers import SupersSerializer
from .models import Supers
from supers import serializers


@api_view(['GET', 'POST'])
def supers_list(request):
    supers = Supers.objects.all()
    if request.method == 'GET':
        serializers = SupersSerializer(supers, many=True)
        return Response(serializers.data)
      
    elif request.method =='POST':
        serializer = SupersSerializer(data=request.data)
        serializer.is_valid(raise_exception= True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)






@api_view (['GET', 'PUT', 'DELETE'])
def super_details(request, pk):
    super = get_object_or_404(Supers, pk=pk)
    if request.method == 'GET':
        serializers = SupersSerializer(super)
        return Response(serializers.data)
    # elif request.method == 'PUT':
    #     serializers = SupersSerializer(super.data)
    #     serializers.is_valid(raise_exception=True)
    #     serializers.save()
    #     return Response(serializers.data)
    # elif request.method == 'DELETE':
    #     return Response(status.HTTP_204_NO_CONTENT)

