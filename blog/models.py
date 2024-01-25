from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.
class Category(models.Model):
    category_name     = models.CharField(max_length=50)
    
    def __str__(self):
        return self.category_name

# ================================================================ start blog
class Blog(models.Model):
    author            = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_title        = models.CharField(max_length=100)
    blog_description  = models.TextField()
    category          = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="category")
    post_date         = models.DateTimeField(auto_now_add=True)
    is_public         = models.BooleanField(default=True)
    slug              = models.CharField(max_length=1000, null=True, blank=True)
    likes             = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    like_count        = models.PositiveIntegerField(default=0)
   
    

    def __str__(self):
        return self.blog_title

    
    def save(self,*args,**kwargs):
        self.slug  = slugify(self.blog_title)
        super(Blog,self).save(*args,**kwargs) 
        
    def update_like_count(self):
        self.like_count = self.likes.count()
        self.save()
        
      

# ================================================================ start blogcomment         

class BlogComment(models.Model):
    description      = models.TextField()
    author           = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment_date     = models.DateTimeField(auto_now_add=True)
    blog             = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return f'{str(self.blog)} - {str(self.description)}'
    
    
    
    
class NestedComment(models.Model):
    text             = models.TextField()
    author           = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment_date     = models.DateTimeField(auto_now_add=True)
    comment          = models.ForeignKey(BlogComment, on_delete=models.CASCADE)
    

    def __str__(self):
        return f' {str(self.comment)} - {str(self.text)}'