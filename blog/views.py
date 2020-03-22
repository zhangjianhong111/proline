from django.shortcuts import render

from .models import blog
# Create your views here.
def blog_page(request):
    
    blogs=blog.objects
    return render(request,'blog.html',{'blog':blogs})