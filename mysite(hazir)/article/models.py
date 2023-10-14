from django.db import models
from ckeditor.fields import RichTextField

import article
# Create your models here.

class Article(models.Model):
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazan")
    title=models.CharField(max_length=50,verbose_name="Basliq")
    content=RichTextField()
    created_date=models.DateTimeField(auto_now_add=True,verbose_name="Yaranma Tarixi")
    article_image=models.FileField(blank=True,null=True,verbose_name="Təklifə şəkil əlavə et")
   
   
    def __str__(self) :
        return self.title

    
    class Meta:
        ordering = ['-created_date']


class Comment(models.Model):
    article=models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="Təklif",related_name="comments")
    comment_author=models.CharField(max_length=50,verbose_name="Ad:")
    comment_content=models.CharField(max_length=200,verbose_name="Rəy")
    comment_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
        
    class Meta:
        ordering = ['-comment_date']