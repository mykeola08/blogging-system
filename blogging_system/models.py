from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify


class Category(models.Model):
    category = models.CharField(max_length=150)

    def __str__(self):
        return '{}'.format(self.category)


def create_slug(title):
    slug = slugify(title)
    qs = Post.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        slug = "%s-%s" %(slug, qs.first().id)
    return slug


class Post(models.Model):
    slug = models.SlugField(null=True, blank=True, unique=True)
    title = models.CharField(max_length=250)
    # thumbnail = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    intro = models.TextField(max_length=1000)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        # force_insert = False, force_update = False, using = None,
        # update_fields = None
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Author(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)

    def __str__(self):
        return self.name

