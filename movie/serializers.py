from rest_framework import serializers
from .models import MovieCategory, MovieInformation

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieCategory
        fields = '__all__'
        # depth = 3

class MovieInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieInformation
        fields = '__all__'



























