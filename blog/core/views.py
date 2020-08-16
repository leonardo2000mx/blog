from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,"core/index.html")

def blog(request):
    return render(request,"core/blog.html")

def post(request):
    return render(request,"core/post.html")