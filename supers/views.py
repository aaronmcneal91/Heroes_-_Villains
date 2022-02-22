
from tokenize import Ignore
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from super_type.models import Super_Type

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
def supers_detail(request, pk):
    super = get_object_or_404(Supers, pk=pk)
    if request.method == 'GET':
        serializers = SupersSerializer(super)
        return Response(serializers.data)
    elif request.method == 'PUT':
        super = get_object_or_404(Supers, pk=pk)
        serializers = SupersSerializer(super, data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





# @api_view(['GET'])
# def supers_list(request):
    
#     type_param = request.query_param.get('type')
#     supers = Super_Type.objects.all()
#     if request.method =='GET':

#         type_param = request.query_param.get(Super_Type)
#         if type_param == 'hero':
#             supers = supers.filter(super_type_id=1)
#             return Response(supers)
#         elif type_param == 'villain':
#             supers =supers.objects.filter(super_type_id=2)
#             return Response(supers)
#         else:
#             supers = Supers.objects.all()
#         return Response(serializers, statu=status.HTTP_200_OK)
    





