from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import *
# from django.urls import reverse

class BlogCommentSerializer(serializers.ModelSerializer):
    blog = serializers.StringRelatedField(read_only=True)
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = BlogComment
        fields = "__all__"
        
class NestedCommentSerializer(serializers.ModelSerializer):
    comment = BlogCommentSerializer(read_only=True)
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = NestedComment
        fields = "__all__"
   
        
        
        

class BlogSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Blog
        fields = "__all__"
    


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    category_name = serializers.CharField()
    category = BlogSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = "__all__"