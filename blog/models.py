from django.db import models
from django import forms

# Create your models here.
class BlogsPost(models.Model):
    title=models.CharField(max_length=150)
    body=models.TextField()
    timestamp=models.DateTimeField()
    #为了给模型设置默认顺序，需要创建一个名为Meta的内部类，在其中设置一个名为ordering的属性
    class Meta:
        ordering=('-timestamp',)
class BlogsPostForm(forms.ModelForm):
    class Meta:
        model=BlogsPost
        exclude=('timestamp',)