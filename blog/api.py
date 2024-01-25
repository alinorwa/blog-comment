from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view ,  permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


# ========================================================= start the category

@api_view(['GET'])
def get_all_categories(request):
    categories = Category.objects.all()  
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)




@api_view(['POST'])
def create_category(request):
    if request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )
    
    
@api_view(['GET'])
def get_one_category(request, category_id):
    try:
        category = Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CategorySerializer(category)
    return Response(serializer.data)

@api_view(['PUT'])
def update_category(request, category_id):
    try:
        category = Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_category(request, category_id):
    try:
        category = Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# ========================================================= end the category



# ========================================================= start the blog
@api_view(['POST'])
def create_blog(request):
    if request.method == 'POST':
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_blogs(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)


# def home(requset):
#     return render(requset , 'home.html')



@api_view(['GET'])
def get_one_blog(request, blog_id):
    try:
        blog = Blog.objects.get(pk=blog_id)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = BlogSerializer(blog)
    return Response(serializer.data)



@api_view(['PUT'])
def update_blog(request, blog_id):
    try:
        blog = Blog.objects.get(pk=blog_id)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    
    
    
      

@api_view(['DELETE'])
def delete_blog(request, blog_id):
    try:
        blog = Blog.objects.get(pk=blog_id)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# =========================================================== end the blog 




# =========================================================== start the comment 
@api_view(['POST'])
def create_comment(request, blog_id):
    try:
        blog = Blog.objects.get(pk=blog_id)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        serializer = BlogCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(blog=blog)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_comments(request, blog_id):
    try:
        blogl = Blog.objects.get(pk=blog_id)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    comments = BlogComment.objects.filter(blog=blogl)
    serializer = BlogCommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
def update_delete_comment(request, comment_id):
    try:
        comment = BlogComment.objects.get(pk=comment_id)
    except BlogComment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = BlogCommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# =========================================================== end the comment 


# =========================================================== start the like blog 

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_dislike_blog(request, blog_id):
    try:
        blog = Blog.objects.get(pk=blog_id)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user

    if user in blog.likes.all():
        # User has already liked the blog, so dislike it
        blog.likes.remove(user)
    else:
        # User has not liked the blog, so like it
        blog.likes.add(user)

    blog.update_like_count()

    serializer = BlogSerializer(blog)
    return Response(serializer.data)
# =========================================================== end the like blog




# =========================================================== start the nested comment
@api_view(['GET'])
def all_nested_comment(request):
    nested_comment = NestedComment.objects.all()
    serializer = NestedCommentSerializer(nested_comment, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_one_nested_comment(request, pk):
    try:
        nested_comment = NestedComment.objects.get(pk=pk)
    except NestedComment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = NestedCommentSerializer(nested_comment)
    return Response(serializer.data)


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def create_nested_comment(request, blog_comment_id):
    try:
        blog_comment = BlogComment.objects.get(pk=blog_comment_id)
    except BlogComment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        serializer = NestedCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(comment=blog_comment)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

@api_view(['PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def update_delete_nested_comment(request, nested_comment_id):
    try:
        nested_comment = NestedComment.objects.get(pk=nested_comment_id)
    except NestedComment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = NestedCommentSerializer(nested_comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        nested_comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    

# =========================================================== end the nested comment 





