from django.shortcuts import render
from .models import Post

# Create your views here.

# # helper functions
# def get_date(post):
#     # return post.get('date')
#     return post['date']
def starting_page(request):
    # sorted_post=post.sort(key=get_date)
    # sorted_post=sorted(post, key=get_date)
    # latest_post=sorted_post[-3:]
    posts=Post.objects.all().order_by("-date")[:3]
    return render(request,'blog/index.html', {"post":posts})

def posts(request):
    all_posts=Post.objects.all().order_by("-date")
    return render(request,'blog/allposts.html',{
        "posts":all_posts})

def post_detail(request,slug):
    identify_post= Post.objects.all().get(slug=slug)
    return render(request,'blog/post-detail.html',{"post":identify_post,"tags":identify_post.tags.all()})
"""   identify_post=next(my_post for my_post in all_posts if my_post['slug']==slug)"""