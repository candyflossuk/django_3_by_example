from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from django.views.generic import ListView
from .forms import EmailPostForm
from django.core.mail import send_mail

# Create your views here - a view is just Python function that receives a web req and returns a response
# All logic to return desired response goes inside the view
# Views can be defined as class methods - the advantages are that organizing code related to HTTP methods is cleaner
# Class based views allow for multiple inheritance (to encourage re use)


class PostListView(ListView):
    queryset = Post.published.all()  # Use a specific QuerySet for retrieving objects
    context_object_name = "posts"  # Use context variable posts for query results
    paginate_by = 3  # Paginate the result - display 3 objects per page
    template_name = "blog/post/list.html"  # Use custom templat to render page


def post_list(request):  # request param required by all views
    object_list = Post.published.all()
    paginator = Paginator(
        object_list, 3
    )  # 3 posts per page - Instantiate Paginator class with number of objects to display per page
    page = request.GET.get(
        "page"
    )  # Get the page GET param indicating current page number
    try:
        posts = paginator.page(
            page
        )  # obtain the objects for the desired page by calling page() of Paginator
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    # Use render() to render the list of posts with the template
    # Takes request context into account (template context processors are callables that set variables into the context)
    return render(request, "blog/post/list.html", {"page": page, "posts": posts})


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


def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status="published")  # Retrieve post
    sent = False
    if request.method == "POST":
        # Form was submitted
        form = EmailPostForm(
            request.POST  # contains the submitted data
        )  # Use same view for displaying and processing
        if form.is_valid():  # validates data in form
            # Form fields passed validation
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read {post.title}"
            message = f"Read {post.title} at {post_url}\n\n{cd['name']}'s comments: {cd['comments']}"
            send_mail(subject, message, "admin@myblog.com", [cd["to"]])
            sent = True
    else:
        form = EmailPostForm()  # displays an empty form
        return render(
            request, "blog/post/share.html", {"post": post, "form": form, "sent": sent}
        )
