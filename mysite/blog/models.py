from django.db import models

# Create your models here - each model will create a table

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):

    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published"),
    )

    title = models.CharField(max_length=250)  # Translates to VARCHAR
    slug = models.SlugField(
        max_length=250, unique_for_date="publish"
    )  # Used for URL, unique_for_date prevents duplicate slugs for posts with same publish date and slug
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )  # Many to One (one user can create many blog posts).
    # on_delete - CASCADE will ensure all blog posts by a deleted user are deleted
    body = models.TextField()  # Translates to TEXT
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(
        auto_now=True
    )  # auto_now_add - date is saved automatically when object is created
    updated = models.DateTimeField(auto_now=True)
    # auto_now - date is updated when saving an object
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="draft"
    )  # Can only be from the STATUS_CHOICES given

    class Meta:
        # Contains the metadata - sort results by the 'publish' field in descending order
        ordering = ("-publish",)

    def __str__(self):
        return self.title
