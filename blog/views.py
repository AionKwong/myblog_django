from django.shortcuts import render
from blog.models import BlogsPost,BlogsPostForm
from datetime import datetime
from django.http import HttpResponseRedirect
# Create your views here.
def blog_index(request):
    blog_list=BlogsPost.objects.all()[:10]
    return render(request,'index.html',{'blog_list':blog_list,'form':BlogsPostForm()})
def create_blogpost(request):
    if request.method=='POST':
        form=BlogsPostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)#注意这是表单的save()，不是模型的save()，这个save()返回Blog模型的实例,由于commit=False，因此在调用post.save()之前不会保存数据
            post.timestamp=datetime.now()
            post.save()
    return HttpResponseRedirect('/blog/')