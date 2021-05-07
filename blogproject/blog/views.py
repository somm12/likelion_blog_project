from django.shortcuts import render , get_object_or_404
from .models import Blog

# Create your views here.

def first(request):
    return render(request,'first.html')
def home(request):
    blogs = Blog.objects #클래스 안에 있는 object를 변수에 넣는다. => querySet이라고 한다.
    return render(request,'home.html',{'blogs':blogs})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html',{'details': details})
def about_me(request):
    return render(request, 'about_me.html')
def email(request):
    return render(request, 'email.html')

def github(request):
    return render(request, 'github.html')
def instagram(request):
    return render(request, 'instagram.html')