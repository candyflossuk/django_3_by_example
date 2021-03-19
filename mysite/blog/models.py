from django.db import models

# Create your models here - each model will create a table

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):

    STATUS_CHOICES = (
        ("draft", "DRAFT"),
        ("published", "Published"),
    )
