from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SupersSerializer
from .models import Supers


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



