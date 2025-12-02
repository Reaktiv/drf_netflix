from django.db import models
from rest_framework.fields import CharField


class MovieCategory(models.Model):
    name = models.CharField(max_length=150, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='subcategories', blank=True, null=True)

    def __str__(self):
        if self.parent:
            return f"{self.name}: {self.parent}"
        return f"{self.name}"


class MovieInformation(models.Model):
    category = models.ForeignKey(MovieCategory)
    name = models.CharField(max_length=50)
    studio = models.CharField(max_length=50)







