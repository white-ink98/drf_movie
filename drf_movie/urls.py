"""
URL configuration for drf_movie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from movie.views import *
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'movies', MoviesViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)), # http://127.0.0.1:8000/api/v1/movies/
    # for version without routers
    # path('api/v1/movielist', MoviesViewSet.as_view({'get': 'list'})),
    # path('api/v1/movielist/<int:pk>/', MoviesViewSet.as_view({'put': 'update'})),
]
# version 2
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/v1/movielist', MoviesAPIList.as_view()),
#     path('api/v1/movielist/<int:pk>/', MoviesAPIUpdate.as_view()),
#     path('api/v1/moviedetail/<int:pk>/', MoviesAPIDetailView.as_view()),
# ]

# version1
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/v1/movielist', MoviesAPIView.as_view()),
#     path('api/v1/movielist/<int:pk>/', MoviesAPIView.as_view()),
# ]