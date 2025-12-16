from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import MovieCategory, MovieInformation
from .serializers import CategorySerializer, MovieInformationSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def home_page(request):
    return Response({
        "project": "Netflix Clone API",
        "version": "v1",
        "status": "running 🚀",
        "endpoints": {
            "auth": "/api/v1/auth/",
            "movies": "/api/v1/movies/",
            "categories": "/api/v1/categories/",
            "genres": "/api/v1/genres/",
            "search": "/api/v1/search/",
            "profile": "/api/v1/profile/",
        },
        "docs": "/swagger/ or /redoc/"
    })


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


@api_view(["GET", "POST"])
def movie_list_or_create(request):
    if request.method == "GET":
        category_information = MovieInformation.objects.all()
        serializer = MovieInformationSerializer(category_information, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = MovieInformationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(["GET", "DELETE", "PUT"])
def movie_retrieve_update_or_delete(request, pk):
    try:
        movie = MovieInformation.objects.get(id=pk)
    except MovieCategory.DoesNotExist:
        return Response({"message": "Not found"})
    if request.method == "GET":
        serializer = MovieInformationSerializer(movie)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = MovieInformationSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == "DELETE":
        movie.delete()
        return Response({"message": "deleted"}, status=204)