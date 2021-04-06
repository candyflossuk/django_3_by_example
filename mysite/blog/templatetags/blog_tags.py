from django import template
from django.db.models import Count
from ..models import Post
from django.utils.safestring import mark_safe
import markdown

"""
Each module that contains template tags needs to define register to be a valid tag library.
"""
register = template.Library()


@register.filter(name="markdown")
def markdown_format(text):
    return mark_safe(markdown.markdown(text))


@register.simple_tag
def total_posts():
    """
    Creates a simple tag. The function name doubles up as the tag name. To register with a different name this must
    be stipulated in @register.simple_tag(name='my_tag').

    custom template tags can process any data and add it to any template regardless of the view executed.

    :return: The total number of published Posts
    """
    return Post.published.count()


# Includes the name of the template that will be rendered with the returned values. Inclusion tags have to return a dict
@register.inclusion_tag("blog/post/latest_posts.html")
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by("-publish")[:count]
    return {"latest_posts": latest_posts}


@register.simple_tag
def get_most_commented_posts(count=5):
    # Build query set using annotate
    return Post.published.annotate(total_comments=Count("comments")).order_by(
        "-total_comments"
    )[:count]
