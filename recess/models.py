from django.db import models

# Create your models here.


class League(models.Model):
    name = models.CharField(max_length=100)
    manager = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    sport = models.CharField(max_length=100)
    rules = models.TextField()

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=5)
    date = models.DateField()
    info = models.TextField()
    image = models.TextField()
    league = models.ForeignKey(
        League, on_delete=models.CASCADE, related_name='games')

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.CharField(max_length=100)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    game = models.ForeignKey(
        Game, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.author


class Comment(models.Model):
    author = models.CharField(max_length=100)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.author


class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    city = models.CharField(max_length=100)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name
