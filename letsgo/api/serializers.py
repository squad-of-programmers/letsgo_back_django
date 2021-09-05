from django.contrib.auth.models import User
from django.db.models.fields.related import RelatedField
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from .models import Blogger, Tour

from typing import Any


# class BloggerJSONSocialNetworksEncoder(DjangoJSONEncoder):
#     def default(self, obj: Any) -> Any:
#         if isinstance(obj, CustomType):
#             return str(obj)
#         return super().default(obj)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', )


# class BloggerProfileListSerializer(serializers.ModelSerializer):
#     user = UserSerializer()

#     title = serializers.CharField(max_length=255)
#     # email = serializers.EmailField()
#     created_at = serializers.DateTimeField()
#     tours = serializers.SlugRelatedField(slug_field='slug', read_only=True, many=True)
    
#     # gender = serializers.CharField(max_length=1) # choices


#     class Meta:
#         model = BloggerProfile


# class BloggerProfileDetailSerializer(serializers.ModelSerializer):
#     user = UserSerializer()

#     title = serializers.CharField(max_length=255)
#     email = serializers.EmailField()
#     created_at = serializers.DateTimeField()
#     tours = serializers.SlugRelatedField(slug_field='slug', read_only=True, many=True)

#     class Meta:
#         model = BloggerProfile


class BloggerListSerializer(serializers.ModelSerializer):

    title = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    created_at = serializers.DateTimeField()
    tours = serializers.SlugRelatedField(slug_field='slug', read_only=True, many=True)


    # def create(self, validated_data):
    #     return Blogger(**validated_data)

    def update(self, instance, validated_data):
        ...
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.created = validated_data.get('created', instance.created)
    #     return instance

    def created_at_validate():
        ...


    class Meta:
        model = Blogger


class BloggerDetailSerializer(serializers.ModelSerializer):

    title = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    created_at = serializers.DateTimeField()
    tours = serializers.SlugRelatedField(slug_field='slug', read_only=True, many=True)

    class Meta:
        model = Blogger


class TourListSerializer(serializers.ModelSerializer):

    # title = serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField(format='%Y:%m:%d')
    updated_at = serializers.DateTimeField(format='%Y:%m:%d')
    start_date = serializers.DateField(format='%Y:%m:%d')
    end_date = serializers.DateField(format='%Y:%m:%d')


    class Meta:
        model = Tour
        fields = '__all__'


class TourDetailSerializer(serializers.ModelSerializer):
    
    title = serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField(format="%Y:%m:%d")

    
    class Meta:
        model = Tour
