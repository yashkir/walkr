from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Walk(models.Model):
    '''A full guided tour.'''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}: {self.description[:25]}"

    def get_absolute_url(self):
        #TODO GO TO STOP/DETAIL VIEW
        return ('/')



class Stop(models.Model):
    '''A location that is part of a Walk.'''
    walk = models.ForeignKey(Walk, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    location_text = models.CharField(max_length=256)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.title} ({self.location_text}): {self.description[:25]}"


class Picture(models.Model):
    '''An illustration of a Stop.'''
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    image = models.ImageField()

    def __str__(self):
        return f"{self.title}"
