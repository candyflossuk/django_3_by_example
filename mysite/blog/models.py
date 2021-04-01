from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here - each model will create a table


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status="published")


class Post(models.Model):
    """
    The name of the table 'blog_post' is derived from model metadata - but can be overriden
    'id' - field is automatically created this behaviour can be overriden.
    The 'settings' file will drive out the SQL syntax to use based on the DB that is there.
    """

    objects = (
        models.Manager()
    )  # The default manager - if you want to add your own managers and keep default you must add it
    published = PublishedManager()  # Custom manager

    # Don't use field names that conflict with the Models api - clean, save, delete (for example)
    # For choices, first value in tuple is what is in db, second is displayed by field's form widget
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

    tags = (
        TaggableManager()
    )  # Allows you to add tags to the post, ordering of fields drives ordering in admin UI

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


class Comment(models.Model):
    # FK to associate a single comment with a single post. Many to 1 - each post can have many comments
    # related_name attribute - names the attribute you use for the relationship from one object to the other,
    # this allows you to do comment.post and post.comments.all()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    """
    auto_now_add - set field to now when object is first created. If you set a value for this field
    on creation - it will be ignored unless auto_now_add=True. Useful for 'created' fields
    auto_now_add, auto_now and default are mutually exclusive - any combination will cause an error.
    auto_now_add and auto_now (as of writing) - when set to True will set editable=False and blank=True
    """
    created = models.DateTimeField(auto_now_add=True)
    """
    auto_now - automatically sets the field to now every time the object is saved. Useful for last-modified fields.
    This value cannot be overridden. This is only updated on Model.save()
    """
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ("created",)

    def __str__(self):
        return f"Comment by {self.name} on {self.post}"
