from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

from forums.models import Thread, get_comments_forum
import uuid

User = get_user_model()


def make_unique_picture_filename(instance, filename):
    return uuid.uuid4().hex[:6] + filename[filename.rfind('.'):]


class Walk(models.Model):
    '''A full guided tour.'''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    is_public = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    comment_thread = models.OneToOneField(Thread, null=True, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        if self._state.adding:
            comment_thread = Thread.objects.create(
                title=f"Walk: {self.title}",
                forum=get_comments_forum(),
                author=self.user,
            )
            comment_thread.save()
            self.comment_thread = comment_thread

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}: {self.description[:25]}"

    def get_absolute_url(self):
        return reverse ('walk_detail', args=[str(self.id)])


class Stop(models.Model):
    '''A location that is part of a Walk.'''
    walk = models.ForeignKey(Walk, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    location_text = models.CharField(max_length=256)
    order = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.title} ({self.location_text}): {self.description[:25]}"

    def get_absolute_url(self):
        return reverse ('walk_detail', args=[str(self.walk.id)])


class Picture(models.Model):
    '''An illustration of a Stop.'''
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    image = models.ImageField(upload_to=make_unique_picture_filename)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse ('stop_detail', args=[str(self.stop.walk.id), str(self.stop.id)])
