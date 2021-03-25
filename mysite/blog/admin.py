from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post, Comment


# The admin.register decorator does the same thing as admin.site.register().
# Registering the ModelAdmin class it decorates
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # list_display allows you to set the fields you want to display on the admin object page
    list_display = ("title", "slug", "author", "publish", "status")
    # list_filter - allows you to filter results by the fields included here
    list_filter = ("status", "created", "publish", "author")
    # search bar is included as list of searchable fields is included
    search_fields = ("title", "body")
    # slug is populated automatically when you type the title
    prepopulated_fields = {"slug": ("title",)}
    # Author is now displayed with a lookup widget - that scales better than a drop-down
    raw_id_fields = ("author",)
    # navigation links to navigate through date hierarchy are included
    date_hierarchy = "publish"
    # Posts are ordered by STATUS and PUBLISH columns by default - specified using ordering attribute
    ordering = ("status", "publish")


@admin.register(Comment)
class ContentAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "post", "created", "active")
    list_filter = ("active", "created", "updated")
    search_fields = ("name", "email", "body")
