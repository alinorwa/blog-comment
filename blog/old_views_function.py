from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import BlogSerializer
from .models import Blog


@api_view(['GET','POST'])
def show_all_Blog_List(request):
    if request.method == 'GET':
        all_blog    = Blog.objects.filter(is_public=True)
        serializser = BlogSerializer(all_blog , many=True)
        return Response(serializser.data,status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializser = BlogSerializer(data=request.data)
        if serializser.is_valid():
            serializser.save()
            return Response(serializser.data , status=status.HTTP_201_CREATED)
        else:
            return Response(serializser.errors , status=status.HTTP_400_BAD_REQUEST)
#_____________________________________________________________________
@api_view(['GET','PUT','DELETE'])
def blog_detail(request,pk):
    if request.method == 'GET':
        blog         = Blog.objects.get(is_public=True , pk=pk)
        serializser  = BlogSerializer(blog , many=False)
        return Response(serializser.data , status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        blog         = Blog.objects.get(pk=pk)
        serializser  = BlogSerializer(blog , data=request.data)
        if serializser.is_valid():
            serializser.save()
            return Response(serializser.data , status=status.HTTP_200_OK)
        else:
            return Response(serializser.errors , status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        blog         = Blog.objects.get(pk=pk)
        blog.delete()
        return Response({'message':'the blog was deleted seccsefuly'} , status=status.HTTP_200_OK)
            