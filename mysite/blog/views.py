from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here - a view is just Python function that receives a web req and returns a response
# All logic to return desired response goes inside the view


def post_list(request):  # request param required by all views
    posts = Post.published.all()
    # Use render() to render the list of posts with the template
    # Takes request context into account (template context processors are callables that set variables into the context)
    return render(request, "blog/post/list.html", {"posts": posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        slug=post,
        status="published",
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    return render(request, "blog/post/detail.html", {"post": post})
