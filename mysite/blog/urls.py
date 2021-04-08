"""
A URL pattern is composed of a string pattern, view and optionally
a name to name the URL project wide.

When a URL match is found - Django imports the view of the matching
URL pattern and executes it, passing an instance of HTTPRequest
and the kwarg or args.

Creating a URLs per application is the best way to make your applications reusable by other projects
"""
from django.urls import path
from . import views
from .feeds import LatestPostsFeed

app_name = "blog"  # application namespace (organize URLs by application)

urlpatterns = [
    # post views
    path("", views.post_list, name="post_list"),
    path("tag/<slug:tag_slug>/", views.post_list, name="post_list_by_tag"),
    # path(
    # "", views.PostListView.as_view(), name="post_list"
    # ),  # Use the class based view instead
    # Use angle brackets to capture values from URL
    path(
        "<int:year>/<int:month>/<int:day>/<slug:post>/",
        views.post_detail,
        name="post_detail",
    ),
    path("<int:post_id>/share/", views.post_share, name="post_share"),
    path("feed/", LatestPostsFeed(), name="post_feed"),
]
