from django.urls import path
from .views import *
from .api import *


urlpatterns = [
    # path('' , BlogListCreateView.as_view()),
    # path('category/' , CategoryListeCreateView.as_view()),
    
    # path('detail/<int:pk>/' , BlogDetialView.as_view()),
    # # category
    # path('category-detail/<int:pk>/' , CategoryDetailView.as_view()),
    # # comment
    # path("comment/<int:blog_id>/", BlogCommentListCreateView.as_view(), name="blog_comment_list"),
    # path("blog/<int:blog_id>/comment/<int:comment_id>/", BlogCommentDetailView.as_view(), name="blog_comment_detail"),
    
    # from api.py blog
    path('', get_all_blogs, name='get_all_blogs'),
    # path('home/', home, name='get_all_blogs'),
    path('create_blog/', create_blog, name='create_blog'),
    path('get_one_blog/<int:blog_id>/', get_one_blog, name='get_one_blog'),
    path('update_blog/<int:blog_id>/', update_blog, name='update_blog'),
    path('delete_blog/<int:blog_id>/', delete_blog, name='delete_blog'),
    
     #  from api category
    path('get_all_categories/', get_all_categories, name='get_all_categories'),
    path('create_category/', create_category, name='create_category'),
    path('get_one_category/<int:category_id>/', get_one_category, name='get_one_category'),
    path('update_category/<int:category_id>/', update_category, name='update_category'),
    path('delete_category/<int:category_id>/', delete_category, name='delete_category'),
   
    
    
    # from api comment
    path('create_comment/<int:blog_id>/', create_comment, name='create_comment'),
    path('get_comments/<int:blog_id>/', get_comments, name='get_comments'),
    path('update_delete_comment/<int:comment_id>/', update_delete_comment, name='update_delete_comment'),
    
    
    
    
    # ======================================================================================= nested comment 
    path('all_nested_comment/',all_nested_comment),
    path('get_one_nested_comment/<int:pk>/', get_one_nested_comment, name='get_one_nested_comment'),
    path('create_nested_comment/<int:blog_comment_id>/', create_nested_comment, name='create_nested_comment'),
    path('update_delete_nested_comment/<int:nested_comment_id>/', update_delete_nested_comment, name='update_delete_nested_comment'),
    
    
    # from api like blog 
    path('like_blog/<int:blog_id>/', like_dislike_blog, name='like_dislike_blog'),
    
    
]
