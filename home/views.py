from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("This is a view which is created by me")

def paths(request):
    # displays paths of all the blogposts inside the django webdite
    # fetch all the slugs from the blog post table
    context = {
        'heading' : "django tutorials 1",
        'content' : "this is the best django tutorial on this entire planet"
    }
    return HttpResponse("This is a view which is created by me")
