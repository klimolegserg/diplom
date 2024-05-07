from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()

    def __str__(self):
        return self.text

    objects = models.Manager()


# для доп. задания
# class PostImage(models.Model):
#     ...


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    publication = models.ForeignKey(Post, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)

    objects = models.Manager()


class Comment(models.Model):
    author = models.IntegerField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.text

    objects = models.Manager()
