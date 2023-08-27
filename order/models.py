from django.db import models
from auth_r.models import User
from job.models import Job


# Create your models here.
class Order(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order for {self.job.title} by {self.buyer.username}"
