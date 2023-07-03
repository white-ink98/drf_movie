import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Movies


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = "__all__"
# class MoviesModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


# class MoviesSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     category_id = serializers.IntegerField()

    # def create(self, validated_data):
    #     return Movies.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.time_update = validated_data.get('time_update', instance.time_update)
    #     instance.is_published = validated_data.get('is_published', instance.is_published)
    #     instance.category_id = validated_data.get('category_id', instance.category_id)
    #     instance.save()
    #     return instance

    #   class Meta:
    #         model = Movies
    #         fields = ('title', 'category_id')

#   def encode():
#       model = MoviesModel('Terminator Fatum', "Content: American fantasy action film")
#       model_serialize = MoviesSerializer(model)
#       print(model_serialize.data, type(model_serialize.data), sep='/n')
#       json = JSONRenderer().render(model_serialize.data)
#       print(json)

# def decode():
#     stream = io.BytesIO(b'{"title":"Terminator Fatum", "content":"Content: American fantasy action film"}')
#     data = JSONParser().parse(stream)
#     serializer = MoviesSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)