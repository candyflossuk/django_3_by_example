from django import template
from ..models import Post

"""
Each module that contains template tags needs to define register to be a valid tag library.
"""
register = template.Library()


@register.simple_tag
def total_posts():
    """
    Creates a simple tag. The function name doubles up as the tag name. To register with a different name this must
    be stipulated in @register.simple_tag(name='my_tag').

    custom template tags can process any data and add it to any template regardless of the view executed.

    :return: The total number of published Posts
    """
    return Post.published.count()
