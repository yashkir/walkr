from django.urls import reverse
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()
COMMENTS_FORUM_NAME = "Walk Comments"
COMMENTS_FORUM_DESCRIPTION = "A special forum to comment on walks."


def get_comments_forum():
    forum, created = Forum.objects.get_or_create(
        title=COMMENTS_FORUM_NAME,
        defaults={'description': COMMENTS_FORUM_DESCRIPTION},
    )
    return forum


class Forum(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return self.title


class Thread(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)
    post_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Post(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    reply_to = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)
    position = models.PositiveIntegerField()
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post {self.position} in Thread: {self.thread}"
