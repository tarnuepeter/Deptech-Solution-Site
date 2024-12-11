from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime
from ckeditor.fields import RichTextField


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home")


class Post(models.Model):
    title = models.CharField(max_length=225)
    title_tag = models.CharField(max_length=225)
    slug = models.SlugField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # body = models.TextField()
    body = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="blog_posts")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="posts"
    )
    header_image = models.ImageField(null=True, blank=True, upload_to="feature_images/")
    snippet = models.CharField(
        max_length=2000, default="click on the link above to read in more detail"
    )

    class Meta:
        ordering = ("-created_at",)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse("article-detail", args=(str(self.id)))
        return reverse("home")


class Inquery(models.Model):
    name = models.CharField(default="", max_length=100)
    email = models.EmailField(default="tarnue@gmail.com", max_length=200)
    contact = models.IntegerField(default=8888, null=True, blank=True)
    subject = models.CharField(default="urgent", max_length=300)
    message = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse("article-detail", args=(str(self.id)))
        return reverse("home")


SERVICES = (
    ("Web Application", "Web Application"),
    ("Mobile Application", "Mobile Application"),
    ("Expert Website Design", "Exper Website Design"),
    ("Tech Consultancy", "Tech Consultancy"),
    ("Data Transcription", "Data Transcriptions"),
    ("Research Questionnaire Design", "Research Questionnaire Design"),
    ("Data Entry", "Data Entry"),
)


class Booking(models.Model):
    name = models.CharField(max_length=100, default='')
    address = models.TextField(default='')
    business = models.CharField(max_length=100)
    contact = models.IntegerField()
    email = models.EmailField()
    service = models.CharField(choices=SERVICES, max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse("article-detail", args=(str(self.id)))
        return reverse("home")
