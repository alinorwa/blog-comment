from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *
from .models import *


# ================================================================================== get all , post
class BlogView(APIView):
    def get(self, request, format=None):
        all_blog = Blog.objects.filter(is_public=True)
        serializer = BlogSerializer(all_blog, many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)
    def post(self , request):
        serializser = BlogSerializer(data=request.data)
        if serializser.is_valid():
            serializser.save()
            return Response(serializser.data , status=status.HTTP_201_CREATED)
        else:
            return Response(serializser.errors , status=status.HTTP_400_BAD_REQUEST)
        
# ================================================================================== detail update delete       
class BlogDetailView(APIView):
    def get(self , request , pk):
        blog         = Blog.objects.get(is_public=True , pk=pk)
        serializser  = BlogSerializer(blog , many=False)
        return Response(serializser.data , status=status.HTTP_200_OK)
       
    def put(self ,request ,pk):
        blog         = Blog.objects.get(pk=pk)
        serializser  = BlogSerializer(blog , data=request.data)
        if serializser.is_valid():
            serializser.save()
            return Response(serializser.data , status=status.HTTP_200_OK)
        else:
            return Response(serializser.errors , status=status.HTTP_400_BAD_REQUEST)   
    
    def delete(self , request ,pk):
        blog         = Blog.objects.get(pk=pk)
        blog.delete()
        return Response({'message':'the blog was deleted seccsefuly'} , status=status.HTTP_200_OK)   
    
    
class CategoryListView(APIView):
    def get(self , request ):
        category     = Category.objects.all()
        serializers  = CategorySerializer(category , many=True)
        return Response(serializers.data , status=status.HTTP_200_OK) 
    
class CategoryDetailView(APIView):         
    def get(self , request , pk ):
        category     = Category.objects.get(pk=pk)
        serializers  = CategorySerializer(category )
        return Response(serializers.data , status=status.HTTP_200_OK)      


