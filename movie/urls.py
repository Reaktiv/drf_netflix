from django.urls import path
from movie import views
urlpatterns = [
    path('', views.home_page),
    path('category/', views.category_list_or_create),
    path('category/<int:pk>/', views.category_retrieve_update_or_delete),
    path('movie/', views.movie_list_or_create),
    path('movie/<int:pk>/', views.movie_retrieve_update_or_delete),
]