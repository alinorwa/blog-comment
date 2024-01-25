from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import Blog, BlogComment


class BlogSerializer(serializers.Serializer):
    id          = serializers.IntegerField(read_only=True)
    blog_title        = serializers.CharField()
    author      = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    blog_description  = serializers.CharField()
    post_date   = serializers.DateTimeField()
    is_public   = serializers.BooleanField()
    slug        = serializers.CharField() 
    
    def create(self, validated_data):
        return Blog.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.blog_title = validated_data.get('blog_title', instance.blog_title)
        instance.author = validated_data.get('author', instance.author)
        instance.blog_description = validated_data.get('blog_description', instance.blog_description)
        instance.post_date = validated_data.get('post_date', instance.post_date)
        instance.is_public = validated_data.get('is_public', instance.is_public)
        instance.slug  = validated_data.get('slug ', instance.slug )
        instance.save()
        return instance