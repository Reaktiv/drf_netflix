from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import MovieCategory
from .serializers import CategorySerializer


@api_view(['GET', 'POST'])
def category_list_or_create(request):
    if request.method == 'GET':
        categories  = MovieCategory.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def category_retrieve_update_or_delete(request, pk):
    try:
        category = MovieCategory.objects.get(id=pk)
    except MovieCategory.DoesNotExist:
        return Response({'message': 'Not found'})
    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return  Response(serializer.errors)

    elif request.method == "DELETE":
        category.delete()
        return Response({'message': 'Deleted'}, status=204)


