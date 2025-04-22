from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):   #defines our model(object)  models.Model indicates post is django model,so django knows that it should be saved in database
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)   #link to another model like a connection between tables in database. It requires 2 things model ur linking to and what to do when linked object is deletd. Here it means if author is deleted post will be deleted
    title = models.CharField(max_length=200)   #syntax to define text with limited char
    text = models.TextField()                  #for long text without limit
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)  # blank=True allows field to be left empty  .//  null=Tru allows null values

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

