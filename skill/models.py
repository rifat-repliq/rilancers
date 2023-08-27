from django.db import models


# Create your models here.
class Skill(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title
