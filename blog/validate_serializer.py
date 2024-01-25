from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import Blog, BlogComment

class BlogSerializer(serializers.ModelSerializer):
    # author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Blog
        fields = "__all__"
    
    # validate ============================================= start validate
    # def validate_blog_title(self, value): 
    #     if len(value) < 3:
    #         raise serializers.ValidationError('blog title is very short')
    #     else:
    #         return value  
    # def validate(self , data):
    #     if data['blog_title'] == data['blog_description']:
    #         raise serializers.ValidationError('blog-title and description can not be same !')  
    #     else:
    #         return data  
    # ======================================================= end validate 