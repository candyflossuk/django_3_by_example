from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9  # max is 1

    def items(self):  # Returns queryset of objects to include in the sitemap
        return Post.published.all()

    def lastmod(self, obj):  # Returns the last time the object was modified
        return obj.updated
