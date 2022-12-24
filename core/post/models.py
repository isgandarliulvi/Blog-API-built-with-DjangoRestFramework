from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length = 150)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Profile(models.Model):
    name = models.CharField(max_length = 100)
    surname = models.CharField(max_length = 150)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name = "posts")
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name = "profile")
    title = models.CharField(max_length = 200)
    content = models.TextField()
    release_date = models.DateField(auto_now = True)
    update_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = "comments")
    commenter = models.ForeignKey(User, on_delete = models.CASCADE, null = True, related_name = "user_comments")
    comment = models.TextField(blank = True, null = True)
    rating = models.PositiveIntegerField(
        validators = [MinValueValidator(1), MaxValueValidator(10)],

    )

    def __str__(self):
        return str(self.rating)
