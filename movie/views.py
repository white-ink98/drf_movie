from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Movies
from .serializers import MoviesSerializer


class MoviesApiView(APIView):
    def get(self, request):
        m = Movies.objects.all()
        #my_list = Movies.objects.all().values()
        return Response({'posts': MoviesSerializer(m, many=True).data})

    def post(self, request):
        serializer = MoviesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = Movies.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            category_id=request.data['category_id']
        )
        return Response({'post': MoviesSerializer(post_new).data})
# class MoviesApiView(generics.ListAPIView):
#     queryset = Movies.objects.all()
#     serializer_class = MoviesSerializer
