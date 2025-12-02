from rest_framework import serializers
from .models import MovieCategory

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieCategory
        fields = '__all__'
        # depth = 3


























