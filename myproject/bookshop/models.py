from django.db import models
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(max_length=129)
    publishment_date = models.DateField(default=timezone.now)  # дата публикации
    created_date = models.DateTimeField(auto_now_add=True)      # дата создания записи
    price = models.FloatField()
    description = models.CharField(max_length=250)
    author = models.CharField(max_length=30)
    number_of_views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
