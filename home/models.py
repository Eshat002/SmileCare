from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify
from django.urls import reverse
import re
from django.contrib.auth import get_user_model

User = get_user_model()


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question


class Contact(models.Model):
    name = models.CharField(
        max_length=100,
    )
    phone = models.CharField(
        max_length=15,
    )

    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=False)

    featured_image = models.ImageField(
        upload_to="featured_images/",
        default="featured_images/default_image.jpg",
        validators=[FileExtensionValidator(["png", "jpg", "jpeg", "gif"])],
   
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            # Generate a unique slug based on the title
            self.slug = slugify(self.title)

            # Ensure slug is unique
            original_slug = self.slug
            count = 2
            while Article.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{count}"
                count += 1

        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.title
