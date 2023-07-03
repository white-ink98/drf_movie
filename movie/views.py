from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Movies
from .serializers import MoviesSerializer


class MoviesApiView(APIView):
    def get(self, request):
        my_list = Movies.objects.all().values()
        return Response({'posts': list(my_list)})

    def post(self, request):
        post_new = Movies.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            category_id=request.data['category_id']
        )
        return Response({'post': model_to_dict(post_new)})
# class MoviesApiView(generics.ListAPIView):
#     queryset = Movies.objects.all()
#     serializer_class = MoviesSerializer
