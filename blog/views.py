from django.shortcuts import render,get_object_or_404

from .models import blog
# Create your views here.
def blog_page(request):
    
    blogs=blog.objects
    return render(request,'blog.html',{'blog':blogs})


def blog_text(request,blog_id):
    blog_text=get_object_or_404(blog,pk=blog_id)
    #blogs = blog.objects
    return render(request, 'blog_text.html',{'blog':blog_text})


