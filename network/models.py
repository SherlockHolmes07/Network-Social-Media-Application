from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Contains name, dob, about, img(url), followers(int), following(int)."""
    name = models.CharField(max_length=100,blank=True)
    dob = models.DateField(blank=True,null=True)
    about = models.TextField(max_length=1000,blank=True)
    img = models.URLField(default="https://t4.ftcdn.net/jpg/02/66/60/17/360_F_266601726_NCXy2AIRecYluwp5BUKOXQAWo35Seilr.jpg")
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.username} created"


class Post(models.Model):
    """Contains user, time(auto_now_add), content, likes"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="all_posts")
    time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=1000,null=False)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user} created a post."


class Following(models.Model):
    """follower -> followed"""
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="get_followers")
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name="get_followed")
    
    def __str__(self):
        return f"{self.follower} follows {self.followed}."
    class Meta:
     unique_together = ('follower', 'followed',)

class Like(models.Model):
    """user -> post"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="get_Likers")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="get_posts")
    
    def __str__(self):
        return f"{self.user.username} liked post with id:{self.post.id}."
