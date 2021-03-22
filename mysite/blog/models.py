from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here - each model will create a table


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status="published")


class Post(models.Model):

    objects = (
        models.Manager()
    )  # The default manager - if you want to add your own managers and keep default you must add it
    published = PublishedManager()  # Custom manager

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
        auto_now_add=True
    )  # auto_now_add - date is saved automatically when object is created
    updated = models.DateTimeField(auto_now=True)
    # auto_now - date is updated when saving an object
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="draft"
    )  # Can only be from the STATUS_CHOICES given

    class Meta:
        # Contains the metadata - sort results by the 'publish' field in descending order
        ordering = ("-publish",)
        # default_manager_name can specify a different default manager

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Use in templates to link to specific posts
        :return: Canonical URL for the Post model that can be used as a specific URL for the model resource
        """
        # self.publish.year/month/day - The year reference does not exist until it is dynamically built at runtime
        # noinspection PyUnresolvedReferences
        return reverse(
            "blog:post_detail",
            args=[self.publish.year, self.publish.month, self.publish.day, self.slug],
        )
