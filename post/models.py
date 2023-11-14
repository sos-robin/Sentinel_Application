from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone


# Create your models here.
User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
#hero slider section
class Homepage_slider(models.Model):
    quote_title = models.CharField(max_length=200)
    image = models.ImageField()
    quote_content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.quote_title
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    content_post = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    comment_count =models.PositiveBigIntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    featured = models.BooleanField()
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('single-post',kwargs=[self.slug])

 
    def __str__(self):
        return self.title

class Comment(models.Model):

    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return f'Comment by {self.name}'


class About(models.Model):
    ministry_name = models.CharField(max_length=50)
    ministry_history = models.TextField()
    ministry_pic = models.ImageField()
    ministry_mission = models.TextField()
    ministry_mission_pic = models.ImageField()
    latest_news_title = models.CharField(max_length=50)
    latest_news = models.TextField()
    team_description =models.TextField()

    def __str__(self):
        return self.ministry_name
class TeamMember(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    profile_pic = models.ImageField()
    team_member_desription =models.TextField()

    def __str__(self):
        return self.name
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name
