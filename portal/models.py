from  django.db import models


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False) 
    short_description = models.CharField(max_length=300)
    image = models.ImageField(upload_to="news/")

    def __str__(self):
        return self.title