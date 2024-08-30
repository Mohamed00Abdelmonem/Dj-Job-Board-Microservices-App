from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=20000)
    publish_date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)

    auther_id = models.IntegerField()


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


    def __str__(self):
        return self.title



class PostLikes(models.Model):
    post = models.ForeignKey(Post,related_name='post_likes', on_delete=models.CASCADE)
    user_id = models.IntegerField()  

    def __str__(self) -> str:
        return str(self.post)  


class Comment(models.Model):
    user_id = models.IntegerField()
    post = models.ForeignKey(Post, related_name='comment_post', on_delete=models.CASCADE)
    content = models.TextField(max_length=2000)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return str(self.post)